from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views import generic

import zipfile
import io
import os

from adn3 import mixins
from courses.mixins import IsTeacherOfCourseMixin
from .forms import *
from adn3.services import is_teacher_of, is_assistant_of_agenda, is_coordinator

from . import services
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from courses.models import Agenda


class TestMixin(mixins.CourseMixin):
    def get_test(self):
        return get_object_or_404(Test, pk=self.kwargs['test_pk'])


class VersionMixin(TestMixin):
    def get_version(self):
        return get_object_or_404(Version, pk=self.kwargs['version_pk'])


# Test Views
# ==========
class TestDetail(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.DetailView):
    model = Test


class TestDownloadAll(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.View):
    def get(self, *args, **kwargs):
        test = get_object_or_404(Test, pk=self.kwargs['pk'])

        s = io.BytesIO()

        zf = zipfile.ZipFile(s, 'w')

        for version in test.version_set.all():
            for answer in version.studentsanswers_set.all():
                if answer.document:
                    _, ext = os.path.splitext(answer.document.path)
                    zf.write(answer.document.path, answer.student.email.replace('@', '__') + ext)

        zf.close()

        resp = HttpResponse(s.getvalue(), content_type="application/x-zip-compressed")
        resp['Content-Disposition'] = 'attachment; filename=%s' % (
                test.name.replace(' ', '_')
                .replace('á', 'a')
                .replace('é', 'e')
                .replace('í', 'i')
                .replace('ó', 'o')
                .replace('ú', 'u')
                .replace('ñ', 'n')
                + '.zip')
        resp['Content-length'] = s.tell()

        return resp


class TestCreate(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.CreateView):
    model = Test
    form_class = TestForm

    def get_form(self, form_class=None):
        form = super(TestCreate, self).get_form(form_class)
        form.fields['session'].queryset = self.get_course().session_set
        return form

    def form_valid(self, form):
        form.instance.course = self.get_course()
        form.instance.owner = self.request.user
        return super(TestCreate, self).form_valid(form)


class TestReviewListView(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.DetailView):
    model = Test
    template_name = 'tests/test_review_students_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.get_course()
        return context


class TestReviewStatisticsView(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.DetailView):
    model = Test
    template_name = 'tests/test_review_statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['correctIncorrects'] = {}
        for version in self.get_object().version_set.all():
            info = {}
            # Corrects vs Incorrects
            for i, question in enumerate(version.question_set.all()):
                correct, incorrect = question.get_correct_incorrect_answers()
                if correct != 0 or incorrect != 0:
                    info[i] = {
                        'question': question,
                        'correct': correct,
                        'incorrect': incorrect,
                        'correctPercentage': correct * 100 / (correct + incorrect),
                        'incorrectPercentage': incorrect * 100 / (correct + incorrect),
                    }

            context['correctIncorrects'][version.get_letter] = info

        return context


class TestReviewView(IsTeacherOfCourseMixin, TestMixin, generic.DetailView):
    model = StudentsAnswers
    template_name = "tests/test_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = self.get_test()
        context['answers'] = Answer.objects.filter(student=self.get_object().student
                                                   , question__version=self.get_object().version)
        return context

    def post(self, request, *args, **kwargs):
        student_answer = self.get_object()
        qualification = 0

        for key, val in request.POST.items():
            if key != "csrfmiddlewaretoken" and key != "action":
                answer = get_object_or_404(Answer, pk=key)
                answer.correct = True if val == 'true' else False
                answer.save()

                if val == "true":
                    qualification += answer.question.score

        # FIXME: Maybe it's better to get the qualification in real time with an
        # FIXME: object method and not use an attribute to store it every time
        student_answer.qualification = qualification
        student_answer.save()

        tests_list_url = reverse('tests:test_review_list', args=[kwargs['course_pk'], kwargs['test_pk']])
        if request.POST.get('action') == "close-after":
            return HttpResponseRedirect(tests_list_url + '?message=success');
        elif request.POST.get('action') == "next-after":
            next_ = StudentsAnswers.objects.filter(version__test__pk=kwargs['test_pk'], qualification=None).first()
            if next_:
                return HttpResponseRedirect(next_.get_review_url())
            else:
                return HttpResponseRedirect(tests_list_url + '?message=nomore')


class DownloadStudentFileView(IsTeacherOfCourseMixin, mixins.CourseMixin, View):
    model = StudentsAnswers

    def get(self, request, course_pk, test_pk, pk):
        student_answer = get_object_or_404(StudentsAnswers, pk=pk)
        if student_answer.document:
            filename = student_answer.document.name.split('/')[-1]
            response = HttpResponse(student_answer.document, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename =%s' % filename
            return response
        else:
            return HttpResponse("El estudiante no adjuntó un documento")


class TestUpdate(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.UpdateView):
    model = Test
    form_class = TestForm


class TestDelete(IsTeacherOfCourseMixin, mixins.CourseMixin, generic.DeleteView):
    model = Test

    def get_success_url(self):
        return self.get_course().get_tests_url()


# Version Views
# =============
class VersionDetail(IsTeacherOfCourseMixin, TestMixin, generic.DetailView):
    model = Version

    def get_context_data(self, **kwargs):
        context = super(VersionDetail, self).get_context_data(**kwargs)
        context['file_form'] = VersionFileForm(self.object)
        return context


class VersionCreate(IsTeacherOfCourseMixin, TestMixin, View):
    def get(self, request, course_pk, test_pk):
        test = get_object_or_404(Test, pk=test_pk)

        version = Version(test=test)
        version.save()

        return redirect(version.test.get_absolute_url())


class VersionDelete(IsTeacherOfCourseMixin, TestMixin, generic.DeleteView):
    model = Version

    def get_success_url(self):
        return self.get_test().get_absolute_url()


class ToggleTest(UserPassesTestMixin, View):
    def get(self, request, course_pk, pk, agenda_pk, referrer):
        agenda_test = get_object_or_404(AgendaTest, agenda__pk=agenda_pk, test__pk=pk)
        agenda_test.active = not agenda_test.active
        agenda_test.save()
        return HttpResponseRedirect(referrer)

    def test_func(self):
        agenda = get_object_or_404(Agenda, pk=self.kwargs['agenda_pk'])
        return is_assistant_of_agenda(self.request.user, agenda)


class VersionDuplicateView(IsTeacherOfCourseMixin, TestMixin, generic.DetailView):
    model = Version
    template_name = "tests/version_confirm_duplicate.html"

    def post(self, request, *args, **kwargs):
        new_version = self.get_object()
        new_version.pk = None
        new_version.save()
        for q in self.get_object().question_set.all():
            services.duplicate_question(q, new_version)
        return redirect(self.get_test().get_absolute_url())


# FIXME: Change?
def version_attach_file(request, version_pk, course_pk, test_pk):
    version = get_object_or_404(Version, pk=version_pk)

    form = VersionFileForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        if version.file.name:
            version.file.delete()

        version.file = form.cleaned_data['file']
        version.save()

    return redirect(version.get_absolute_url())


# Question Views
# ==============
class ChoiceQuestionCreate(IsTeacherOfCourseMixin, VersionMixin, generic.CreateView):
    model = ChoiceQuestion
    form_class = ChoiceQuestionForm

    def form_valid(self, form):
        form.instance.version = self.get_version()
        response = super(ChoiceQuestionCreate, self).form_valid(form)

        for i in range(1, 6):
            text = form.cleaned_data['alternative_' + str(i)]
            if not text:
                continue

            correct = True if form.cleaned_data['correct'] == i else False
            alternative = Alternative(text=text, correct=correct, question=self.object, index=i)
            alternative.save()

        return response

    def get_success_url(self):
        return self.get_version().get_absolute_url()


class ChoiceQuestionUpdate(IsTeacherOfCourseMixin, VersionMixin, generic.UpdateView):
    model = ChoiceQuestion
    form_class = ChoiceQuestionForm

    def get_form(self, form_class=None):
        form = super(ChoiceQuestionUpdate, self).get_form(form_class)
        for alt in self.object.alternative_set.all():
            if alt.correct:
                form.fields['correct'].initial = str(alt.index)

            form.fields['alternative_' + str(alt.index)].initial = alt.text

        return form

    def form_valid(self, form):
        response = super(ChoiceQuestionUpdate, self).form_valid(form)

        self.object.alternative_set.all().delete()

        for i in range(1, 6):
            text = form.cleaned_data['alternative_' + str(i)]
            if not text:
                continue

            correct = True if form.cleaned_data['correct'] == i else False
            alternative = Alternative(text=text, correct=correct, question=self.object, index=i)
            alternative.save()

        return response

    def get_success_url(self):
        return self.get_version().get_absolute_url()


class ChoiceQuestionDelete(IsTeacherOfCourseMixin, VersionMixin, generic.DeleteView):
    model = ChoiceQuestion

    def get_success_url(self):
        return self.get_version().get_absolute_url()


class TextQuestionCreate(IsTeacherOfCourseMixin, VersionMixin, generic.CreateView):
    model = TextQuestion
    form_class = TextQuestionForm

    def form_valid(self, form):
        form.instance.version = self.get_version()
        return super(TextQuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return self.get_version().get_absolute_url()


class TextQuestionUpdate(IsTeacherOfCourseMixin, VersionMixin, generic.UpdateView):
    model = TextQuestion
    form_class = TextQuestionForm

    def get_success_url(self):
        return self.get_version().get_absolute_url()


class TextQuestionDelete(IsTeacherOfCourseMixin, VersionMixin, generic.DeleteView):
    model = TextQuestion

    def get_success_url(self):
        return self.get_version().get_absolute_url()


class NumericalQuestionCreate(IsTeacherOfCourseMixin, VersionMixin, generic.CreateView):
    model = NumericalQuestion
    form_class = NumericalQuestionForm

    def form_valid(self, form):
        form.instance.version = self.get_version()
        return super(NumericalQuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return self.get_version().get_absolute_url()


class NumericalQuestionUpdate(IsTeacherOfCourseMixin, VersionMixin, generic.UpdateView):
    model = NumericalQuestion
    form_class = NumericalQuestionForm

    def get_success_url(self):
        return self.get_version().get_absolute_url()


class NumericalQuestionDelete(IsTeacherOfCourseMixin, VersionMixin, generic.DeleteView):
    model = NumericalQuestion

    def get_success_url(self):
        return self.get_version().get_absolute_url()
