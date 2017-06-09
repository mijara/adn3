from django.views import generic
from django.views import View
from tests.models import Version, StudentsAnswers, Test, Answer
from public import services

from adn3.services import is_assistant_of
from courses.models import Agenda, Course

from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone


class AgendaListView(generic.ListView):
    model = Agenda
    template_name = 'public/agenda_list.html'

    def get_queryset(self):
        return self.request.user.inscriptions.all() | self.request.user.assistants.all()


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'public/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # check if the user is assistant of the course.
        context['assistant'] = None
        for agenda in self.object.agenda_set.all():
            if is_assistant_of(self.request.user, agenda):
                context['assistant'] = agenda

        # Check test status
        # 0: The test has not been performed
        # 1: The test is in progress
        # 2: The test is over
        context['test_set'] = []
        for test in self.object.test_set.all():
            test_as_dict = test.__dict__
            test_as_dict['time'] = test.get_timeout_display
            test_as_dict['session'] = test.session.number
            test_as_dict['pk'] = test.pk

            for version in test.version_set.all():
                try:
                    student_version = StudentsAnswers.objects.get(student=self.request.user, version=version)
                except ObjectDoesNotExist:
                    student_version = None

                if student_version:
                    test_as_dict['status'] = student_version.get_status()
                elif not student_version:
                    test_as_dict['status'] = 0

            context['test_set'].append(test_as_dict)
        return context


class TestPreConfirmationView(generic.DetailView):
    model = Test
    template_name = 'public/preconfirmation_test.html'

    def get(self, request, *args, **kwargs):
        test = self.get_object()
        student_version = StudentsAnswers.objects.filter(student=self.request.user)

        for sv in student_version:
            if sv.version.test == test and sv.get_status() == 2:
                return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': test.course.pk}))
            elif sv.version.test == test and sv.get_status() == 1:
                return HttpResponseRedirect(reverse('public:test_detail', kwargs={'pk': sv.version.pk}))

        else:
            return super().get(self, request, *args, **kwargs)


class TestVersionAssignView(generic.DetailView):
    model = Test

    def get(self, request, *args, **kwargs):
        test = self.get_object()
        student_version = StudentsAnswers.objects.filter(student=self.request.user)

        for sv in student_version:
            if sv.version.test == test and sv.get_status() == 2:
                return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': test.course.pk}))
            elif sv.version.test == test and sv.get_status() == 1:
                return HttpResponseRedirect(reverse('public:test_detail', kwargs={'pk': sv.version.pk}))
        else:
            version = services.assign_version(test)

            student_version = StudentsAnswers(student=request.user, version=version)
            student_version.save()

            # Once the students has a assigned version, create empty answers
            for question in version.question_set.all():
                services.create_empty_answers(question, request.user)

            return HttpResponseRedirect(reverse('public:test_detail', kwargs={'pk': version.pk}))


class TestDetailView(generic.DetailView):
    model = Version
    template_name = 'public/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['studentanswer'] = StudentsAnswers.objects.get(student=self.request.user,
                                                                   version=self.object)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': version.test.course.pk}))

        context['answers'] = Answer.objects.filter(student=self.request.user, question__version=self.get_object())
        return context

    def get(self, request, *args, **kwargs):
        version = self.get_object()
        try:
            student_version = StudentsAnswers.objects.get(student=self.request.user, version=version)
        except ObjectDoesNotExist:
            student_version = None

        if student_version and student_version.get_status() == 2:
            return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': version.test.course.pk}))
        elif not student_version:
            return HttpResponseRedirect(reverse('public:preconfirmation_test', kwargs={'pk': version.test.pk}))

        return super().get(self, request, *args, **kwargs)


class UpdateAnswers(View):
    def post(self, request):
        try:
            student_answer = StudentsAnswers.objects.get(student=request.user, version__pk=request.POST['version'])
            if student_answer.get_status() == 1:
                for key in request.POST:
                    services.update_answer(key, request.user, request.POST[key], request.POST['version'])

                for key in request.FILES:
                    services.update_document(request.POST['version'], request.user, request.FILES[key])

                # Update the field 'last_update'
                student_answer.refresh_from_db()
                student_answer.last_update = timezone.now()
                student_answer.save()
                return JsonResponse({
                    'error': False,
                    'message': timezone.localtime(timezone.now()).strftime('%H:%M'),
                    'document': student_answer.document.name
                })

            else:
                return JsonResponse({'error': True, 'message': u'Tiempo excedido'})

        except Exception as e:
            return JsonResponse({'error': True, 'message': e})
