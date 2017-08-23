from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from adn3.constants import YEAR, SEMESTER
from coordination.services import generate_excel
from adn3.services import preregistrations_open, preregistrations_set, \
    is_coordinator

from courses.models import Course
from misc.models import Software


class CoordinatorTestMixin(UserPassesTestMixin):
    def test_func(self):
        return is_coordinator(self.request.user)


class CoordinationIndexView(CoordinatorTestMixin, View):
    def get(self, request):
        current_courses = Course.objects.filter(semester=SEMESTER, year=YEAR)

        return render(request, 'coordination/coordination_index.html', {
            'current_courses': current_courses,
            'software_list': Software.objects.all(),
            'preregistrations_open': preregistrations_open(),
        })


class PreRegistrationExcelView(CoordinatorTestMixin, View):
    def get(self, request):
        course = self.get_course()
        software = self.get_software()

        pr_list = course.preregistration_set.filter(software=software).all()
        content = generate_excel(course, software, pr_list)

        response = HttpResponse(
            content=content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=preinscripciones.xlsx'
        return response

    def get_course(self):
        course_pk = self.request.GET.get('course')

        if course_pk is None:
            raise Http404()

        return get_object_or_404(Course, pk=course_pk)

    def get_software(self):
        software_pk = self.request.GET.get('software')

        if software_pk is None:
            raise Http404()

        return get_object_or_404(Software, pk=software_pk)


class PreRegistrationsToggle(CoordinatorTestMixin, View):
    def get(self, request):
        state = preregistrations_open()
        preregistrations_set(not state)

        return redirect('coordination:coordination_index')
