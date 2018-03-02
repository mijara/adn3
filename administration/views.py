from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User, Group

from courses.models import Course
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

    success_url = reverse_lazy('administration:teacher_create_success')

    def form_valid(self, form):
        form.instance.username = form.instance.email
        form.instance.set_password('temporal')

        response = super().form_valid(form)

        teachers_group = Group.objects.get(name='teachers')
        self.object.groups.add(teachers_group)

        return response


class TeacherSuccessView(AdministratorTestMixin, generic.TemplateView):
    template_name = 'administration/teacher_success.html'


class CourseCreateView(AdministratorTestMixin, generic.CreateView):
    model = Course
    form_class = forms.CourseForm
    template_name = 'administration/course_create.html'

    success_url = reverse_lazy('administration:course_success')


class CourseSuccessView(AdministratorTestMixin, generic.TemplateView):
    template_name = 'administration/course_success.html'
