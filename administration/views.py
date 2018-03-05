from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User, Group

from administration.forms import StudentForm
from adn3.services import get_period_year, get_period_semester
from courses.models import Course, CourseTeacher, Agenda
from misc.models import Setting
from registration.models import Student
from . import forms


class AdministratorTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class AdministrationIndexView(AdministratorTestMixin, generic.TemplateView):
    template_name = 'administration/administration_index.html'


class TeacherCreateView(AdministratorTestMixin, generic.CreateView):
    model = User
    form_class = forms.TeacherForm
    template_name = 'administration/teacher_create.html'

    success_url = reverse_lazy('administration:teacher_success')

    def form_valid(self, form):
        form.instance.username = form.instance.email
        form.instance.set_password('cambiame')

        response = super().form_valid(form)

        teachers_group = Group.objects.get(name='teachers')
        self.object.groups.add(teachers_group)

        return response

    def get_teachers(self):
        group = Group.objects.get(name='teachers')
        return group.user_set.all()


class TeacherSuccessView(AdministratorTestMixin, generic.TemplateView):
    template_name = 'administration/teacher_success.html'


class CourseCreateView(AdministratorTestMixin, generic.CreateView):
    model = Course
    form_class = forms.CourseForm
    template_name = 'administration/course_create.html'

    success_url = reverse_lazy('administration:course_success')

    def get_courses(self):
        courses = Course.objects.filter(year=get_period_year(), semester=get_period_semester())
        return courses.all()


class CourseSuccessView(AdministratorTestMixin, generic.TemplateView):
    template_name = 'administration/course_success.html'


class YearSemesterUpdateView(AdministratorTestMixin, generic.FormView):
    form_class = forms.YearSemesterForm
    template_name = 'administration/yearsemester_form.html'
    success_url = reverse_lazy('administration:administration_index')

    def get_initial(self):
        initial = super().get_initial()

        initial['year'] = get_period_year()
        initial['semester'] = get_period_semester()

        return initial

    def form_valid(self, form):
        """
        Save settings to database.
        """
        setting_year = Setting.objects.get(key='period-year')
        setting_semester = Setting.objects.get(key='period-semester')

        setting_year.value = str(form.cleaned_data['year'])
        setting_semester.value = str(form.cleaned_data['semester'])

        setting_year.save()
        setting_semester.save()

        return super().form_valid(form)


class TeacherCourseCreateView(AdministratorTestMixin, generic.FormView):
    form_class = forms.TeacherCourseForm
    template_name = 'administration/teacher_course_form.html'
    success_url = reverse_lazy('administration:teacher_course_create')

    def form_valid(self, form):
        course = form.cleaned_data['course']
        teacher = form.cleaned_data['teacher']

        if not CourseTeacher.objects.filter(course=course, user=teacher):
            course_teacher = CourseTeacher.objects.create(course=course, user=teacher, coordinates=False)
            course_teacher.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['courses'] = Course.objects.all()
        return context


class CoAssistantCourseCreateView(AdministratorTestMixin, generic.FormView):
    form_class = forms.CoAssistantCourseForm
    template_name = 'administration/co_assistant_course_form.html'
    success_url = reverse_lazy('administration:co_assistant_course_create')

    def form_valid(self, form):
        course = form.cleaned_data['course']
        assistant = form.cleaned_data['assistant']

        if not CourseTeacher.objects.filter(course=course, user=assistant):
            teachers_group = Group.objects.get(name='teachers')

            assistant.groups.add(teachers_group)
            assistant.save()

            course_teacher = CourseTeacher.objects.create(course=course, user=assistant, coordinates=False)
            course_teacher.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['courses'] = Course.objects.all()
        return context


class StudentCreateView(AdministratorTestMixin, generic.CreateView):
    model = User
    form_class = StudentForm
    template_name = 'administration/student_form.html'
    success_url = reverse_lazy('administration:student_success')

    def form_valid(self, form):
        form.instance.username = form.instance.email
        form.instance.set_password('cambiame')

        response = super().form_valid(form)

        campus = form.cleaned_data['campus']
        usm_priority = form.cleaned_data['usm_priority']
        rol = form.cleaned_data['rol']

        Student.objects.create(user=self.object, campus=campus, usm_priority=usm_priority, rol=rol)

        group = Group.objects.get(name='students')
        group.user_set.add(self.object)

        return response


class StudentSuccessView(AdministratorTestMixin, generic.TemplateView):
    template_name = 'administration/student_success.html'


class AssistantCourseSelectView(AdministratorTestMixin, generic.FormView):
    form_class = forms.SelectCourseForm
    template_name = 'administration/course_assistant_select.html'
    success_url = reverse_lazy('administration:assistant_course_create')

    def form_valid(self, form):
        self.form = form
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        course = self.form.cleaned_data['course']
        url = reverse_lazy('administration:assistant_course_create', kwargs={'course_pk': course.pk})
        return url


class AssistantCourseCreateView(AdministratorTestMixin, generic.FormView):
    form_class = forms.AssistantAgendaForm
    template_name = 'administration/course_assistant_create.html'
    success_url = reverse_lazy('administration:assistant_course_create')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['course_pk'] = self.kwargs['course_pk']
        return kwargs

    def form_valid(self, form):
        print('asd')
        agenda = form.cleaned_data['agenda']
        assistant = form.cleaned_data['assistant']
        print(agenda.assistants.all())
        if assistant not in agenda.assistants.all():
            agenda.assistants.add(assistant)
            agenda.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = get_object_or_404(Course, pk=self.kwargs['course_pk'])
        return context

    def get_success_url(self):
        url = reverse_lazy('administration:assistant_course_create', kwargs={'course_pk': self.kwargs['course_pk']})
        return url
