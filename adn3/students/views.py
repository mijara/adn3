from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import generic
from django.views import View
from .models import *
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


class ReserveAttemptCreateView(generic.CreateView):
    model = ReserveAttempt
    form_class = ReserveAttemptForm


class ReserveAttemptDetailView(generic.DetailView):
    model = ReserveAttempt
