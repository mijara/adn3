from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views import generic

from adn3 import mixins
from forms import *


# Test Views
# ==========
class TestList(mixins.CourseMixin, generic.ListView):
    def get_queryset(self):
        return self.get_course().test_set.all()


class TestDetail(generic.DetailView):
    model = Test


class TestCreate(mixins.CourseMixin, generic.CreateView):
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


class TestUpdate(mixins.CourseMixin, generic.UpdateView):
    model = Test
    form_class = TestForm


class TestDelete(mixins.CourseMixin, generic.DeleteView):
    model = Test

    def get_success_url(self):
        return reverse_lazy('tests:test_list', args=[self.get_course().pk])


# Version Views
# =============
class VersionDetail(generic.DetailView):
    model = Version

    def get_context_data(self, **kwargs):
        context = super(VersionDetail, self).get_context_data(**kwargs)
        context['file_form'] = VersionFileForm(self.object)
        return context


class VersionCreate(View):
    def get(self, request, test_pk):
        test = get_object_or_404(Test, pk=test_pk)

        for i, version in enumerate(test.version_set.all()):
            version.index = i + 1
            version.save()

        version = Version(test=test, index=test.version_set.count() + 1)
        version.save()

        return redirect(version.test.get_absolute_url())


class VersionDelete(mixins.TestMixin, generic.DeleteView):
    model = Version

    def get_success_url(self):
        return self.get_test().get_absolute_url()


def version_attach_file(request, version_pk):
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
class ChoiceQuestionCreate(mixins.VersionMixin, generic.CreateView):
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
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])


class ChoiceQuestionUpdate(mixins.VersionMixin, generic.UpdateView):
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
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])


class ChoiceQuestionDelete(mixins.VersionMixin, generic.DeleteView):
    model = ChoiceQuestion

    def get_success_url(self):
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])


class TextQuestionCreate(mixins.VersionMixin, generic.CreateView):
    model = TextQuestion
    form_class = TextQuestionForm

    def form_valid(self, form):
        form.instance.version = self.get_version()
        return super(TextQuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])


class TextQuestionUpdate(mixins.VersionMixin, generic.UpdateView):
    model = TextQuestion
    form_class = TextQuestionForm

    def get_success_url(self):
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])


class TextQuestionDelete(mixins.VersionMixin, generic.DeleteView):
    model = TextQuestion

    def get_success_url(self):
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])


class NumericalQuestionCreate(mixins.VersionMixin, generic.CreateView):
    model = NumericalQuestion
    form_class = NumericalQuestionForm

    def form_valid(self, form):
        form.instance.version = self.get_version()
        return super(NumericalQuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])


class NumericalQuestionUpdate(mixins.VersionMixin, generic.UpdateView):
    model = NumericalQuestion
    form_class = NumericalQuestionForm

    def get_success_url(self):
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])


class NumericalQuestionDelete(mixins.VersionMixin, generic.DeleteView):
    model = NumericalQuestion

    def get_success_url(self):
        return reverse_lazy('tests:version_detail', args=[self.get_version().pk])