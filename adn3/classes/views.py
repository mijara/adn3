from django.shortcuts import render, get_object_or_404, redirect
from models import *
from courses.models import *
from forms import *


def index(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    return render(request, 'classes/index.html', {
        'course': course
    })


def detail(request, course_pk, pk=None):
    course = get_object_or_404(Course, pk=course_pk)

    if pk is None:
        instance = Class()
    else:
        instance = get_object_or_404(Class, pk=pk)

    form = ClassForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.course = course
            instance.save()

            return redirect('classes:index', course_pk=course.pk)

    return render(request, 'classes/detail.html', {
        'course': course,
        'form': form
    })
