from django.http import HttpResponse
from django.shortcuts import render, redirect

from adn3.mixins import CourseMixin
from courses.grades_workbook import generate_course_grades, generate_course_grades_v2
from courses.mixins import IsTeacherOfCourseMixin
from .forms import *
from . import services
from django.views import View


class CourseDetail(IsTeacherOfCourseMixin, CourseMixin, View):
    def get(self, request, course_pk, section='agendas'):
        return render(self.request, 'courses/course_detail.html', {
            'view': self,
            'course': self.get_course(),
            'ACTIVE': section,
            'section': section,
        })


def index(request):
    return redirect('teachers:index')


class GradesView(IsTeacherOfCourseMixin, CourseMixin, View):
    def get(self, request, course_pk):
        return render(request, 'courses/grades.html', {
            'view': self,
            'section': 'grades',
            'ACTIVE': 'grades',
            'course': self.get_course(),
        })


class GradesConfigView(IsTeacherOfCourseMixin, CourseMixin, View):
    def get(self, request, course_pk):
        course = self.get_course()

        try:
            instance = course.grades_config
        except CourseGradesConfig.DoesNotExist:
            instance = CourseGradesConfig()

        general_form = CourseGradesConfigForm(request.POST or None, instance=instance)

        return render(request, 'courses/grades_config.html', {
            'course': course,
            'view': self,
            'section': 'grades',
            'ACTIVE': 'grades',
            'general_form': general_form
        })

    def post(self, request, course_pk):
        course = self.get_course()

        try:
            instance = course.grades_config
        except CourseGradesConfig.DoesNotExist:
            instance = CourseGradesConfig()

        general_form = CourseGradesConfigForm(request.POST or None, instance=instance)

        if general_form.is_valid():
            instance = general_form.save(commit=False)
            instance.course = course
            instance.save()

            services.save_pretests(request.POST)
            services.save_tests(request.POST)
            services.save_sessions(request.POST, services.session_pks(course))

            return redirect('courses:course_grades_config', course_pk=course_pk)

        return render(request, 'courses/grades_config.html', {
            'course': course,
            'view': self,
            'section': 'grades',
            'ACTIVE': 'grades',
            'general_form': general_form
        })


class CourseGradesExcelView(IsTeacherOfCourseMixin, CourseMixin, View):
    def get(self, request, course_pk):
        course = self.get_course()

        content = generate_course_grades(course)

        response = HttpResponse(
            content=content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        response['Content-Disposition'] = 'attachment; filename=notas.xlsx'

        return response


class CourseGradesExcelView2(IsTeacherOfCourseMixin, CourseMixin, View):
    def get(self, request, course_pk):
        course = self.get_course()
        return HttpResponse(content=generate_course_grades_v2(course))


class CourseStudentsExcelView(IsTeacherOfCourseMixin, CourseMixin, View):
    def get(self, request, course_pk):
        course = self.get_course()

        content = services.generate_students_excel(course)

        response = HttpResponse(
            content=content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=estudiantes.xlsx'
        return response
