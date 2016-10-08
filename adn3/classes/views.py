from django.shortcuts import render, get_object_or_404, redirect
from courses.models import *
from forms import *
from datetime import timedelta


def _get_first_available(sessions):
    last = 1
    for s in sessions:
        if s.number > last + 1:
            return last + 1

    return len(sessions) + 1


def index(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    return render(request, 'classes/index.html', {
        'course': course
    })


def detail(request, course_pk, pk=None):
    course = get_object_or_404(Course, pk=course_pk)

    if pk is None:
        # default session.
        instance = Session()

        # set the next available session number.
        instance.number = _get_first_available(course.session_set.all())

        # set this as the start date and the end day as the 5 next days.
        instance.start_date = datetime.now()
        instance.end_date = datetime.now() + timedelta(days=5)
    else:
        instance = get_object_or_404(Session, pk=pk)

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
