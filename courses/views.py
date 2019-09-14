from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.utils.crypto import get_random_string

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

        content = generate_course_grades_v2(course)

        response = HttpResponse(
            content=content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        response['Content-Disposition'] = 'attachment; filename=notas.xlsx'

        return response


class CourseStudentsExcelView(IsTeacherOfCourseMixin, CourseMixin, View):
    def get(self, request, course_pk):
        course = self.get_course()

        content = services.generate_students_excel(course)

        response = HttpResponse(
            content=content,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=estudiantes.xlsx'
        return response


class CourseStudentChangePassword(IsTeacherOfCourseMixin, CourseMixin, generic.FormView):
    template_name = 'courses/student_password.html'
    form_class = PasswordChangeTokenForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['password'] = get_random_string(length=16)
        return data

    def form_valid(self, form):
        self.email = form.cleaned_data['email']
        self.password = form.cleaned_data['password']

        user = User.objects.filter(email=self.email)

        if not user.exists():
            return self.render_to_response({
                'err_message': 'Correo no registrado en el sistema.',
                'password': get_random_string(length=16),
            })

        user = user.get()
        user.set_password(self.password)
        user.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('courses:course_change_password_success',
                            args=[self.get_course().pk]) + f'?password={self.password}&email={self.email}'


class CourseStudentChangePasswordSuccess(IsTeacherOfCourseMixin, CourseMixin, generic.TemplateView):
    template_name = 'courses/student_password_success.html'
