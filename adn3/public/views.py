from django.shortcuts import redirect
from django.views import generic
from django.views import View

from tests.models import Version, StudentsAnswers, Test, Answer
from public import services

from adn3.services import is_assistant_of, is_assistant, preregistrations_open, is_student, is_student_of
from courses.models import Agenda, Course

from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone

from django.contrib.auth.mixins import UserPassesTestMixin


class AgendaListView(UserPassesTestMixin, generic.ListView):
    model = Agenda
    template_name = 'public/agenda_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if (is_assistant(self.request.user)):
            agendas = self.request.user.assistants.all()
            courses = []
            for a in agendas:
                if a.course not in courses:
                    courses.append(a.course)
            context['assistant_courses'] = courses

        return context

    def get(self, request, *args, **kwargs):
        if preregistrations_open():
            return redirect('preregistrations:course_list')

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.inscriptions.all()

    def test_func(self):
        return is_student(self.request.user)


class CourseDetail(UserPassesTestMixin, generic.DetailView):
    model = Course
    template_name = 'public/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['submitted_tests'] = []
        for sv in StudentsAnswers.objects.filter(student=self.request.user, version__test__course=self.get_object()):
            if sv.get_status() == 2:
                context['submitted_tests'].append(sv)
        return context

    def test_func(self):
        return is_student_of(self.request.user, self.get_object())


class TestPreConfirmationView(UserPassesTestMixin, generic.DetailView):
    model = Test
    template_name = 'public/preconfirmation_test.html'

    def get(self, request, *args, **kwargs):
        test = self.get_object()
        try:
            sv = StudentsAnswers.objects.get(student=self.request.user, version__test=test)
            if sv.get_status() == 2:
                return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': test.course.pk}))
            elif sv.get_status() == 1:
                return HttpResponseRedirect(reverse('public:test_detail', kwargs={'pk': sv.version.pk}))

        except ObjectDoesNotExist:
            pass

        return super().get(self, request, *args, **kwargs)

    def test_func(self):
        return is_student_of(self.request.user, self.get_object().course)


class TestVersionAssignView(UserPassesTestMixin, generic.DetailView):
    model = Test

    def get(self, request, *args, **kwargs):
        test = self.get_object()
        if test.active:
            try:
                sv = StudentsAnswers.objects.get(student=self.request.user, version__test=test)
                if sv.get_status() == 2:
                    return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': test.course.pk}))
                elif sv.get_status() == 1:
                    return HttpResponseRedirect(reverse('public:test_detail', kwargs={'pk': sv.version.pk}))
            except ObjectDoesNotExist:
                version = services.assign_version(test)

                sv = StudentsAnswers(student=request.user, version=version)
                sv.save()

                # Once the student has an assigned version, create empty answers
                for question in version.question_set.all():
                    services.create_empty_answers(question, request.user)

                return HttpResponseRedirect(reverse('public:test_detail', kwargs={'pk': version.pk}))
        else:
            return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': test.course.pk}))

    def test_func(self):
        return is_student(self.request.user)


class TestDetailView(UserPassesTestMixin, generic.DetailView):
    model = Version
    template_name = 'public/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # FIXME: self.object??

            context['studentanswer'] = StudentsAnswers.objects.get(student=self.request.user,
                                                                   version=self.object)
        except ObjectDoesNotExist:
            pass

        context['answers'] = Answer.objects.filter(student=self.request.user, question__version=self.get_object())
        return context

    def get(self, request, *args, **kwargs):
        version = self.get_object()
        try:
            sv = StudentsAnswers.objects.get(student=self.request.user, version=version)
            if sv.get_status() == 2:
                return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': version.test.course.pk}))
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('public:test_preconfirmation', kwargs={'pk': version.test.pk}))

        return super().get(self, request, *args, **kwargs)

    def test_func(self):
        return is_student(self.request.user)


class UpdateAnswers(UserPassesTestMixin, View):
    def post(self, request):
        try:
            sv = StudentsAnswers.objects.get(student=request.user, version__pk=request.POST['version'])
            if sv.get_status() == 1:
                for key in request.POST:
                    services.update_answer(key, request.user, request.POST[key], request.POST['version'])

                for key in request.FILES:
                    services.update_document(request.POST['version'], request.user, request.FILES[key])

                # Update the field 'last_update'
                sv.refresh_from_db()
                sv.last_update = timezone.now()

                # If it's the last update, the test is submitted
                if request.POST.get('finish'):
                    sv.submitted = True

                sv.save()
                return JsonResponse({
                    'error': False,
                    'message': timezone.localtime(timezone.now()).strftime('%H:%M'),
                    'document': sv.document.name
                })

            else:
                return JsonResponse({'error': True, 'message': u'Tiempo excedido'})

        except Exception as e:
            return JsonResponse({'error': True, 'message': e})

    def test_func(self):
        return is_student(self.request.user)
