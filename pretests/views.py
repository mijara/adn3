from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from adn3.services import is_teacher_of, is_coordinator
from adn3 import mixins
from .forms import *


class PretestMixin(UserPassesTestMixin, mixins.CourseMixin):
    def get_pretest(self):
        return get_object_or_404(Pretest, pk=self.kwargs['pretest_pk'])

    def test_func(self):
        return is_coordinator(self.request.user) or is_teacher_of(self.request.user, self.get_course())


class PretestDetailView(PretestMixin, mixins.CourseMixin, generic.DetailView):
    model = Pretest


class PretestUpdateView(PretestMixin, mixins.CourseMixin, generic.UpdateView):
    model = Pretest
    form_class = PretestForm


class PretestCreateView(PretestMixin, mixins.CourseMixin, generic.CreateView):
    model = Pretest
    form_class = PretestForm

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super(PretestCreateView, self).form_valid(form)


class PretestDeleteView(PretestMixin, mixins.CourseMixin, generic.DeleteView):
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


class PretestReviewListView(PretestMixin, mixins.CourseMixin, generic.DetailView):
    model = Pretest
    template_name = 'pretests/pretest_review_students_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.get_course()
        return context


class PretestReviewView(PretestMixin, generic.DetailView):
    model = PretestUpload
    template_name = "pretests/pretest_review.html"

    def post(self, request, *args, **kwargs):
        pretest = self.get_object()
        pretest.qualification = request.POST.get('grade')
        pretest.feedback = request.POST.get('feedback')
        pretest.save()

        pretests_list_url = reverse('pretests:pretest_review_list', args=[kwargs['course_pk'], kwargs['pretest_pk']])
        if request.POST.get('action') == "close-after":
            return HttpResponseRedirect(pretests_list_url + '?message=success')
        elif request.POST.get('action') == "next-after":
            next_ = PretestUpload.objects.filter(pretest__pk=kwargs['pretest_pk'], qualification=None).first()
            if next_:
                return HttpResponseRedirect(next_.get_review_url())
            else:
                return HttpResponseRedirect(pretests_list_url + '?message=nomore')