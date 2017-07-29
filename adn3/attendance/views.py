from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Agenda
from .services import *


def show(request, agenda_pk):
    agenda = get_object_or_404(Agenda, pk=agenda_pk)

    try:
        table = create_matrix(agenda)
    except:
        table = None

    return render(request, 'attendance/show.html', {
        'agenda': agenda,
        'table': table,
        'ACTIVE': 'attendance',
        'section': 'attendance',
        'course': agenda.course
    })


def save(request, agenda_pk):
    agenda = get_object_or_404(Agenda, pk=agenda_pk)

    if request.method == 'POST':
        save_matrix(agenda, request.POST)

    return redirect('attendance:show', agenda_pk)
