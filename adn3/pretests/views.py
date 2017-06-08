from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from adn3 import mixins
from .forms import *


class PretestMixin(mixins.CourseMixin):
    def get_pretest(self):
        return get_object_or_404(Pretest, pk=self.kwargs['pretest_pk'])


class PretestDetailView(mixins.CourseMixin, generic.DetailView):
    model = Pretest


class PretestUpdateView(mixins.CourseMixin, generic.UpdateView):
    model = Pretest
    form_class = PretestForm


class PretestCreateView(mixins.CourseMixin, generic.CreateView):
    model = Pretest
    form_class = PretestForm

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super(PretestCreateView, self).form_valid(form)


class PretestDeleteView(mixins.CourseMixin, generic.DeleteView):
    model = Pretest

    def get_success_url(self):
        return self.get_course().get_pretests_url()


class PretestFileCreateView(PretestMixin, generic.CreateView):
    model = PretestFile
    form_class = PretestFileForm

    def form_valid(self, form):
        form.instance.pretest = self.get_pretest()
        return super().form_valid(form)

    def get_success_url(self):
        return self.get_pretest().get_absolute_url()


class PretestFileDeleteView(PretestMixin, generic.DeleteView):
    model = PretestFile

    def get_success_url(self):
        return self.get_pretest().get_absolute_url()
