from django.views import generic
from django.views import View
from tests.models import Version, StudentsAnswers, Test, TextAnswer, NumericalAnswer, ChoiceAnswer, Answer
from tests.models import TextQuestion, NumericalQuestion, ChoiceQuestion, Alternative

from adn3.services import is_assistant_of
from courses.models import Agenda, Course

from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone
import random




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


class PreconfirmationTest(generic.DetailView):
    model = Test
    template_name = 'public/preconfirmation_test.html'

    def get(self, request, *args, **kwargs):
        test = self.get_object()
        student_version = StudentsAnswers.objects.filter(student=self.request.user)
        for sv in student_version:
            if sv.version.test == test and sv.get_status() == 2:
                return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': test.course.pk}))
            elif sv.version.test == test and sv.get_status() == 1:
                return HttpResponseRedirect(reverse('public:do_test', kwargs={'pk': sv.version.pk}))
        else:
            return super().get(self, request, *args, **kwargs)


class AssignTestVersion(generic.DetailView):
    model = Test

    def get(self, request, *args, **kwargs):
        test = self.get_object()
        student_version = StudentsAnswers.objects.filter(student=self.request.user)
        for sv in student_version:
            if sv.version.test == test and sv.get_status() == 2:
                return HttpResponseRedirect(reverse('public:course_detail', kwargs={'pk': test.course.pk}))
            elif sv.version.test == test and sv.get_status() == 1:
                return HttpResponseRedirect(reverse('public:do_test', kwargs={'pk': sv.version.pk}))
        else:
            # Randomly assign a version
            versions = test.version_set.all()
            index = random.randint(0, len(versions) - 1)
            student_version = StudentsAnswers(student=self.request.user, version=versions[index])
            student_version.save()

            # Once the students has a assigned version, create empty answers
            for question in versions[index].question_set.all():

               try:
                   textanswer = TextAnswer(student=request.user, question=question.textquestion)
                   textanswer.save()
               except TextQuestion.DoesNotExist:
                   pass

               try:
                   numericalanswer = NumericalAnswer(student=request.user, question=question.numericalquestion)
                   numericalanswer.save()
               except NumericalQuestion.DoesNotExist:
                   pass

               try:
                   choiceanswer = ChoiceAnswer(student=request.user, question=question.choicequestion)
                   choiceanswer.save()
               except ChoiceQuestion.DoesNotExist:
                   pass

            return HttpResponseRedirect(reverse('public:do_test', kwargs={'pk': versions[index].pk}))


class Test(generic.DetailView):
    model = Version
    template_name = 'public/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['timeleft'] = StudentsAnswers.objects.get(student=self.request.user, version=self.object).get_time_left()
            context['timelapsed'] = self.object.test.timeout - context['timeleft']
            context['last_update'] = StudentsAnswers.objects.get(student=self.request.user, version=self.object).last_update
        except ObjectDoesNotExist:
            context['timeleft'] = self.object.session.test.timeout
            context['timelapsed'] = 0
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
            studentanswer = StudentsAnswers.objects.get(student=request.user, version__pk=request.POST['version'])
            print(studentanswer.get_status())
            if studentanswer.get_status() == 1:
                for key in request.POST:
                    if key not in ['version', 'csrfmiddlewaretoken']:
                        try:
                            answer = TextAnswer.objects.get(pk=key, student=request.user)
                            answer.text = request.POST[key]
                            answer.save()
                        except:
                            pass
                        try:
                            answer = ChoiceAnswer.objects.get(pk=key, student=request.user)
                            answer.alternative = Alternative.objects.get(pk=request.POST[key])
                            answer.save()
                        except:
                            pass
                        try:
                            answer = NumericalAnswer.objects.get(pk=key, student=request.user)
                            answer.number = request.POST[key]
                            answer.save()
                        except:
                            pass
                # Update the field 'last_update'
                date = timezone.now()
                studentanswer = StudentsAnswers.objects.get(student=request.user, version__pk=request.POST['version'])
                studentanswer.last_update = date
                studentanswer.save()
                return JsonResponse({'error': False, 'message': timezone.localtime(timezone.now()).strftime('%H:%M')})
            else:
                return JsonResponse({'error': True, 'message': u'Tiempo excedido'})
        except Exception as e:
            print(type(e))
            print(e)
            return JsonResponse({'error': True, 'message': e})
