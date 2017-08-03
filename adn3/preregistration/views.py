from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from courses.models import Course
from misc.models import Software
from news.models import New
from preregistration.models import PreRegistration
from .forms import PreRegistrationForm
from adn3 import mixins


class CourseDetailView(generic.DetailView, LoginRequiredMixin):
    model = Course
    template_name = 'preregistration/course_detail.html'


class CourseListView(generic.ListView):
    model = Course
    template_name = 'preregistration/course_list.html'

    def get_queryset(self):
        # Filter courses already pre-registered and courses on another campus.
        return super().get_queryset()\
            .exclude(preregistration__student=self.request.user.student)\
            .filter(campus=self.request.user.student.campus)


class NewListView(mixins.CourseMixin, generic.ListView):
    model = New
    template_name = 'preregistration/new_list.html'

    def get_queryset(self):
        return self.get_course().new_set


class PreRegistrationDetailView(generic.DetailView):
    model = PreRegistration


class PreRegistrationCreateView(mixins.CourseMixin, View):
    template_name = 'preregistration/preregistration_form.html'
    form_class = PreRegistrationForm

    def get(self, request, course_pk):
        return render(request, self.template_name, {
            'software_list': Software.objects.all(),
            'course': self.get_course()
        })

    def post(self, request, course_pk):
        preferences = request.POST.getlist('block')
        sel_names = ['first_preference', 'second_preference', 'third_preference',
                     'fourth_preference', 'fifth_preference']
        selections = {}

        for i, p in enumerate(sel_names):
            selections[p] = preferences[i] if len(preferences) > i else ''

        initial = {
            'course': self.get_course().pk,
            'software': self.request.POST.get('software'),
            'previous_experience': self.request.POST.get('previous_experience'),
            'parallel': self.request.POST.get('parallel')
        }
        initial.update(selections)

        form = PreRegistrationForm(initial)

        if form.is_valid():
            form.instance.student = request.user.student
            instance = form.save()
            return redirect(instance.get_absolute_url())

        return render(request, self.template_name, {
            'form': form,
            'course': self.get_course(),
        })


class PreRegistrationDeleteView(generic.DeleteView):
    model = PreRegistration

    def get_success_url(self):
        return reverse_lazy('preregistrations:course_list')
