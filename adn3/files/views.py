from django.shortcuts import render, get_object_or_404, redirect
from django.views.static import serve

from courses.models import Course
from models import *
from forms import *


def index(request, course_pk):
    return render(request, 'files/index.html', {
        'course': get_object_or_404(Course, pk=course_pk)
    })


def download(request, pk):
    course_file = get_object_or_404(CourseFile, pk=pk)

    course_file.downloads += 1
    course_file.save()

    # FIXME: is this a security hazard?
    return redirect(course_file.file.url)


def detail(request, course_pk, pk=None):
    course = get_object_or_404(Course, pk=course_pk)

    if pk is None:
        instance = CourseFile()
    else:
        instance = get_object_or_404(CourseFile, pk=pk)

    form = CourseFileForm(request.POST or None, request.FILES or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.course = course
            instance.save()

            return redirect('files:index', course_pk=course.pk)

    return render(request, 'files/detail.html', {
        'course': course,
        'form': form
    })
