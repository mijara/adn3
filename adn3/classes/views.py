from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import *
from forms import *
from datetime import timedelta
from services import *


def index(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    return render(request, 'classes/index.html', {
        'course': course
    })


def show(request, pk):
    session = get_object_or_404(Session, pk=pk)

    return render(request, 'classes/show.html', {
        'session': session
    })


def detail(request, course_pk, pk=None):
    course = get_object_or_404(Course, pk=course_pk)

    if pk is None:
        # default session.
        instance = Session()

        # set the next available session number.
        instance.number = get_first_available(course.session_set.all())

        # set this as the start date and the end day as the 5 next days.
        instance.start_date = datetime.now()
        instance.end_date = datetime.now() + timedelta(days=5)
    else:
        instance = get_object_or_404(Session, pk=pk)

    form = SessionForm(request.POST or None, instance=instance)

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


def upload(request, pk):
    session = get_object_or_404(Session, pk=pk)

    form = SessionFileForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.session = session
            instance.save()

            return redirect('classes:show', session.pk)

    return render(request, 'classes/upload.html', {
        'session': session,
        'form': form
    })


def remove_file(request, file_pk):
    session_file = get_object_or_404(SessionFile, pk=file_pk)

    session_pk = session_file.session.pk

    session_file.file.delete()
    session_file.delete()

    return redirect('classes:show', session_pk)
