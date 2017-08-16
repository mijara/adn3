from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from adn3.constants import YEAR, SEMESTER
from coordination.services import generate_excel

from courses.models import Course
from misc.models import Software


class CoordinationIndexView(View):
    def get(self, request):
        current_courses = Course.objects.filter(semester=SEMESTER, year=YEAR)
        return render(request, 'coordination/coordination_index.html', {
            'current_courses': current_courses,
            'software_list': Software.objects.all(),
        })


class PreRegistrationExcelView(View):
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
