from django.shortcuts import render, get_object_or_404
from django.views import generic
from models import *
from forms import *
from courses.models import Course


class CourseMixin(object):
    def get_context_data(self, **kwargs):
        context = super(self.__class__.__base__, self).get_context_data(**kwargs)
        context['course'] = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        return context


class TestList(CourseMixin, generic.ListView):
    model = Test


class TestDetail(generic.DetailView):
    model = Test


class TestCreate(CourseMixin, generic.CreateView):
    model = Test
    form_class = TestForm

    def get_form(self, form_class=None):
        form = super(TestCreate, self).get_form(form_class)
        course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        form.fields['session'].queryset = course.session_set
        return form

    def form_valid(self, form):
        course = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        owner = self.request.user

        form.instance.course = course
        form.instance.owner = owner

        return super(TestCreate, self).form_valid(form)


class TestUpdate(CourseMixin, generic.UpdateView):
    model = Test
    form_class = TestForm
