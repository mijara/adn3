from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views import generic

from adn3 import mixins
from .forms import *
from adn3.services import is_teacher_of

from . import services
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


class TestMixin(mixins.CourseMixin):
    def get_test(self):
        return get_object_or_404(Test, pk=self.kwargs['test_pk'])


class VersionMixin(TestMixin):
    def get_version(self):
        return get_object_or_404(Version, pk=self.kwargs['version_pk'])


# Test Views
# ==========
class TestDetail(UserPassesTestMixin, mixins.CourseMixin, generic.DetailView):
    model = Test

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class TestCreate(UserPassesTestMixin, mixins.CourseMixin, generic.CreateView):
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

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class TestReviewListView(UserPassesTestMixin, mixins.CourseMixin, generic.DetailView):
    model = Test
    template_name = 'tests/test_review_students_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.get_course()
        return context

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class TestReviewView(UserPassesTestMixin, TestMixin, generic.DetailView):
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

        # FIXME: Maybe it's better to get the qualification in real time with an object method and not use an attribute to store it every time
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

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class DownloadStudentFileView(UserPassesTestMixin, mixins.CourseMixin, View):
    model = StudentsAnswers

    def get(self, request, course_pk, test_pk, pk):
        student_answer = get_object_or_404(StudentsAnswers, pk=pk)
        if student_answer.document:
            filename = student_answer.document.name.split('/')[-1]
            response = HttpResponse(student_answer.document, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename =%s' % filename
            return response
        else:
            return HttpResponse("El estudiante no adjuntó un documento")

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class TestUpdate(UserPassesTestMixin, mixins.CourseMixin, generic.UpdateView):
    model = Test
    form_class = TestForm

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class TestDelete(UserPassesTestMixin, mixins.CourseMixin, generic.DeleteView):
    model = Test

    def get_success_url(self):
        return self.get_course().get_tests_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


# Version Views
# =============
class VersionDetail(UserPassesTestMixin, TestMixin, generic.DetailView):
    model = Version

    def get_context_data(self, **kwargs):
        context = super(VersionDetail, self).get_context_data(**kwargs)
        context['file_form'] = VersionFileForm(self.object)
        return context

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class VersionCreate(UserPassesTestMixin, TestMixin, View):
    def get(self, request, course_pk, test_pk):
        test = get_object_or_404(Test, pk=test_pk)

        version = Version(test=test)
        version.save()

        return redirect(version.test.get_absolute_url())

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class VersionDelete(UserPassesTestMixin, TestMixin, generic.DeleteView):
    model = Version

    def get_success_url(self):
        return self.get_test().get_absolute_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


# FIXME: Change to a class ?
def toggle_test(request, course_pk, pk, referrer):
    test = get_object_or_404(Test, pk=pk)
    test.active = not test.active
    test.save()
    return HttpResponseRedirect(referrer)


class VersionDuplicateView(UserPassesTestMixin, TestMixin, generic.DetailView):
    model = Version
    template_name = "tests/version_confirm_duplicate.html"

    def post(self, request, *args, **kwargs):
        new_version = self.get_object()
        new_version.pk = None
        new_version.save()
        for q in self.get_object().question_set.all():
            services.duplicate_question(q, new_version)
        return redirect(self.get_test().get_absolute_url())

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


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
class ChoiceQuestionCreate(UserPassesTestMixin, VersionMixin, generic.CreateView):
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

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class ChoiceQuestionUpdate(UserPassesTestMixin, VersionMixin, generic.UpdateView):
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

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class ChoiceQuestionDelete(UserPassesTestMixin, VersionMixin, generic.DeleteView):
    model = ChoiceQuestion

    def get_success_url(self):
        return self.get_version().get_absolute_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class TextQuestionCreate(UserPassesTestMixin, VersionMixin, generic.CreateView):
    model = TextQuestion
    form_class = TextQuestionForm

    def form_valid(self, form):
        form.instance.version = self.get_version()
        return super(TextQuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return self.get_version().get_absolute_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class TextQuestionUpdate(UserPassesTestMixin, VersionMixin, generic.UpdateView):
    model = TextQuestion
    form_class = TextQuestionForm

    def get_success_url(self):
        return self.get_version().get_absolute_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class TextQuestionDelete(UserPassesTestMixin, VersionMixin, generic.DeleteView):
    model = TextQuestion

    def get_success_url(self):
        return self.get_version().get_absolute_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class NumericalQuestionCreate(UserPassesTestMixin, VersionMixin, generic.CreateView):
    model = NumericalQuestion
    form_class = NumericalQuestionForm

    def form_valid(self, form):
        form.instance.version = self.get_version()
        return super(NumericalQuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return self.get_version().get_absolute_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class NumericalQuestionUpdate(UserPassesTestMixin, VersionMixin, generic.UpdateView):
    model = NumericalQuestion
    form_class = NumericalQuestionForm

    def get_success_url(self):
        return self.get_version().get_absolute_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())


class NumericalQuestionDelete(UserPassesTestMixin, VersionMixin, generic.DeleteView):
    model = NumericalQuestion

    def get_success_url(self):
        return self.get_version().get_absolute_url()

    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course())
