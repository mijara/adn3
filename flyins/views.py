from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views import View

from adn3.services import preregistrations_open
from courses.models import Course
from misc.models import Software
from news.models import New
from .models import FlyIn
from .forms import FlyInForm
from adn3 import mixins


class FlyInsActiveMixin(UserPassesTestMixin):
    def test_func(self):
        return preregistrations_open()


class CourseListView(FlyInsActiveMixin, generic.ListView):
    model = Course
    template_name = 'flyins/course_list.html'

    def get_queryset(self):
        # Filter courses already pre-registered and courses on another campus.
        return super().get_queryset().exclude(status=False)


class NewListView(FlyInsActiveMixin, mixins.CourseMixin, generic.ListView):
    model = New
    template_name = 'flyins/new_list.html'

    def get_queryset(self):
        return self.get_course().new_set


class FlyInDetailView(FlyInsActiveMixin, generic.DetailView):
    model = FlyIn


class FlyInCreateView(FlyInsActiveMixin, mixins.CourseMixin, View):
    template_name = 'flyins/preregistration_form.html'
    form_class = FlyInForm

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
            'parallel': self.request.POST.get('parallel'),
            'first_name': self.request.POST.get('first_name'),
            'last_names': self.request.POST.get('last_names'),
            'rol': self.request.POST.get('rol'),
            'usm_priority': self.request.POST.get('usm_priority'),
        }
        initial.update(selections)

        form = FlyInForm(initial)

        if form.is_valid():
            instance = form.save()
            return redirect(instance.get_absolute_url())

        return render(request, self.template_name, {
            'form': form,
            'course': self.get_course(),
        })
