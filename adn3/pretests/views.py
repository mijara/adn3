from django.shortcuts import render, get_object_or_404, redirect
from courses.models import *
from models import *
from forms import *


def index(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    return render(request, 'pretests/index.html', {
        'course': course
    })


def show(request, pk):
    pretest = get_object_or_404(Pretest, pk=pk)

    return render(request, 'pretests/show.html', {
        'pretest': pretest
    })


def detail(request, course_pk, pk=None):
    course = get_object_or_404(Course, pk=course_pk)

    if pk is None:
        instance = Pretest()
    else:
        instance = get_object_or_404(Pretest, pk=pk)

    form = PretestForm(request.POST or None, instance=instance)
    form.fields['start_session'].queryset = course.session_set
    form.fields['end_session'].queryset = course.session_set

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.course = course
            instance.save()

            return redirect('pretests:show', pk=instance.pk)

    return render(request, 'pretests/detail.html', {
        'course': course,
        'form': form
    })


def upload(request, pk):
    pretest = get_object_or_404(Pretest, pk=pk)

    form = PretestFileForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pretest = pretest
            instance.save()

            return redirect('pretests:show', pretest.pk)

    return render(request, 'pretests/upload.html', {
        'pretest': pretest,
        'form': form
    })
