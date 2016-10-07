from django.shortcuts import render, get_object_or_404, redirect
from forms import *
from courses.models import *


def index(request, pk):
    return render(request, 'news/index.html', {
        'course': get_object_or_404(Course, pk=pk)
    })


def show(request, pk):
    new = get_object_or_404(New, pk=pk)

    return render(request, 'news/show.html', {
        'new': new
    })


def create(request, course_pk, pk=None):
    course = get_object_or_404(Course, pk=course_pk)

    if pk is None:
        instance = New(course=course)
    else:
        instance = get_object_or_404(New, pk=pk)

    form = NewForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.course = course
            instance.save()

            return redirect('courses:show', course.pk)

    return render(request, 'news/create.html', {
        'course': course,
        'form': form
    })
