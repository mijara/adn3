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
# ==========
class VersionDetail(generic.DetailView):
    model = Version


class VersionCreate(View):
    def get(self, request, test_pk):
        test = get_object_or_404(Test, pk=test_pk)
        version = Version(test=test)
        version.save()

        return redirect(version.test.get_absolute_url())


class VersionDelete(mixins.TestMixin, generic.DeleteView):
    model = Version

    def get_success_url(self):
        return self.get_test().get_absolute_url()
