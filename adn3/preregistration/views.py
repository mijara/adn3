from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic
from courses.models import Course
from preregistration.models import PreRegistration
from .forms import PreRegistrationForm
from adn3 import mixins


class PreRegistrationDetailView(generic.DetailView):
    model = PreRegistration


class PreRegistrationCreateView(mixins.CourseMixin, generic.TemplateView):
    template_name = 'preregistration/preregistration_form.html'
    form_class = PreRegistrationForm

    def post(self, request, course_pk):
        preferences = request.POST.getlist('block')
        sel_names = ['first_preference', 'second_preference', 'third_preference',
                     'fourth_preference', 'fifth_preference']
        selections = {}

        for i, p in enumerate(sel_names):
            selections[p] = preferences[i] if len(preferences) > i else ''

        initial = {'course': self.get_course().pk}
        initial.update(selections)

        form = PreRegistrationForm(initial)

        if form.is_valid():
            form.instance.student = request.user.student
            instance = form.save()
            return redirect(instance.get_absolute_url())

        pass


class CourseDetailView(generic.DetailView, LoginRequiredMixin):
    model = Course
    template_name = 'preregistration/course_detail.html'


class CourseListView(generic.ListView):
    model = Course
    template_name = 'preregistration/course_list.html'
