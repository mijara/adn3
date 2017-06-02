from django.shortcuts import render, get_object_or_404, redirect

from adn3 import mixins
from .forms import *
from . import services
from django.views import generic


class CourseDetail(mixins.CourseMixin, generic.View):
    def get(self, request, course_pk, section='agendas'):
        return render(self.request, 'courses/course_detail.html', {
            'course': self.get_course(),
            'section': section
        })


def index(request):
    return redirect('self:index')


def grades(request, pk):
    return render(request, 'courses/grades.html', {
        'course': get_object_or_404(Course, pk=pk)
    })


def grades_config(request, pk):
    course = get_object_or_404(Course, pk=pk)

    try:
        instance = course.grades_config
    except CourseGradesConfig.DoesNotExist:
        instance = CourseGradesConfig()

    general_form = CourseGradesConfigForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if general_form.is_valid():
            instance = general_form.save(commit=False)
            instance.course = course
            instance.save()

            services.save_pretests(request.POST)
            services.save_tests(request.POST)
            services.save_sessions(request.POST, services.session_pks(course))

            return redirect('courses:grades', pk=pk)

    return render(request, 'courses/grades_config.html', {
        'course': course,
        'general_form': general_form
    })
