from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from .forms import *
from .services import validate_secret


class StudentCreateView(View):
    def get(self, request):
        user_form = UserForm(prefix='user')
        student_form = StudentForm(prefix='student')

        return render(request, 'students/student_form.html', context={
            'user_form': user_form,
            'student_form': student_form,
        })

    def post(self, request):
        user_form = UserForm(request.POST, prefix='user')
        student_form = StudentForm(request.POST, prefix='student')

        if user_form.is_valid() and student_form.is_valid():
            email = user_form.cleaned_data['email']
            secret = student_form.cleaned_data['secret']

            if validate_secret(email, secret):
                user_form.instance.username = email
                user = user_form.save()

                students_group = Group.objects.get(name='students')
                students_group.user_set.add(user)

                student = Student(
                    user=user,
                    rol=student_form.cleaned_data['rol'],
                    usm_priority=student_form.cleaned_data['usm_priority'])
                student.save()

                return redirect('students:student_success')
            else:
                student_form.add_error('secret', 'Código secreto inválido')

        return render(request, 'students/student_form.html', context={
            'user_form': user_form,
            'student_form': student_form,
        })


class StudentSuccessView(generic.TemplateView):
    template_name = 'students/student_success.html'


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'students/student_update.html'

    def get_object(self, queryset=None):
        return self.request.user.student


class StudentPasswordUpdateView(View):
    def get(self, request):
        form = PasswordChangeForm(self.request.user)

        return render(request, 'students/student_password_update.html', context={
            'form': form,
        })

    def post(self, request):
        form = PasswordChangeForm(self.request.user, data=self.request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(self.request.user.student.get_absolute_url())

        return render(request, 'students/student_password_update.html', context={
            'form': form,
        })


class ReserveAttemptCreateView(generic.CreateView):
    model = ReserveAttempt
    form_class = ReserveAttemptForm


class ReserveAttemptDetailView(generic.DetailView):
    model = ReserveAttempt
