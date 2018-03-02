from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

from adn3.mixins import CourseMixin
from adn3.services import is_teacher_of, is_coordinator, is_superteacher_of
from courses.grades_workbook import generate_course_grades
from .forms import *
from . import services
from django.views import View


class IsTeacherOfCourseMixin(UserPassesTestMixin):
    def test_func(self):
        return is_coordinator(self.request.user) or \
               is_teacher_of(self.request.user, self.get_course()) or \
               is_superteacher_of(self.request.user, self.get_course())


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
        response[
            'Content-Disposition'] = 'attachment; filename=preinscripciones.xlsx'
        return response
