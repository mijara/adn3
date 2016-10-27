from django.shortcuts import render, get_object_or_404, redirect
from models import *
from forms import *
import services


def show(request, pk):
    return render(request, 'courses/show.html', {
        'course': get_object_or_404(Course, pk=pk)
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

            services.save_grades(request.POST)

            return redirect('courses:grades', pk=pk)

    return render(request, 'courses/grades_config.html', {
        'course': course,
        'general_form': general_form
    })
