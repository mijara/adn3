from django.shortcuts import render, get_object_or_404
from courses.models import Agenda


def show(request, agenda_pk):
    agenda = get_object_or_404(Agenda, pk=agenda_pk)

    # build a table for attendance.
    attendance = {}
    max_session_number = 0

    for user in agenda.inscriptions.all():
        attendance[user] = {}

    for assistant in agenda.attendance_set.all():
        max_session_number = max(max_session_number, assistant.session.number)
        attendance[assistant.user][assistant.session.number] = assistant.get_attended_display()

    table = []
    for user, data in attendance.items():
        row = [data[i] if i in data else '-' for i in range(1, max_session_number + 1)]
        table.append([user.get_full_name(), '-'] + row)

    return render(request, 'attendance/show.html', {
        'agenda': agenda,
        'attendance': table,
    })
