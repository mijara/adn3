from django.shortcuts import render, get_object_or_404, redirect
from forms import *
from courses.models import *


def index(request, course_pk):
    return render(request, 'news/index.html', {
        'course': get_object_or_404(Course, pk=course_pk)
    })


def show(request, pk):
    new = get_object_or_404(New, pk=pk)

    return render(request, 'news/show.html', {
        'new': new
    })


def detail(request, course_pk, pk=None):
    course = get_object_or_404(Course, pk=course_pk)

    if pk is None:
        instance = New()
    else:
        instance = get_object_or_404(New, pk=pk)

    form = NewForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.course = course
            instance.save()

            return redirect('news:show', pk=instance.pk)

    return render(request, 'news/detail.html', {
        'course': course,
        'form': form
    })
