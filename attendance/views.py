from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Agenda
from .services import *
from adn3.services import is_teacher_of, is_coordinator
from adn3.mixins import CourseMixin
from django.views import View


class HasAccessToAttendanceMixin(UserPassesTestMixin):
    def test_func(self):
        return is_teacher_of(self.request.user, self.get_course()) or is_coordinator(self.request.user)


class ShowAttendanceView(HasAccessToAttendanceMixin, CourseMixin, View):
    def get(self, request, course_pk, agenda_pk):
        agenda = get_object_or_404(Agenda, pk=agenda_pk)

        try:
            table = create_matrix(agenda)
        except:
            table = None

        return render(request, 'attendance/show.html', {
            'view': self,
            'agenda': agenda,
            'table': table,
            'ACTIVE': 'agendas',
            'section': 'agendas',
            'course': self.get_course()
        })


class SaveAttendanceView(HasAccessToAttendanceMixin, CourseMixin, View):
    def post(self, request, course_pk, agenda_pk):
        agenda = get_object_or_404(Agenda, pk=agenda_pk)
        save_matrix(agenda, request.POST)
        return redirect('attendance:show', course_pk, agenda_pk)
