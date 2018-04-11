from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views import generic
from django.views import View

from adn3 import settings
from .forms import *
from .services import validate_secret


class StudentCreateView(View):
    def get(self, request):
        user_form = UserForm(prefix='user')
        student_form = StudentForm(prefix='student')

        return render(request, 'registration/student_form.html', context={
            'user_form': user_form,
            'student_form': student_form,
        })

    def post(self, request):
        user_form = UserForm(request.POST, prefix='user')
        student_form = StudentForm(request.POST, prefix='student')

        if user_form.is_valid() and student_form.is_valid():
            email = user_form.cleaned_data['email'].lower()

            if User.objects.filter(username=email).exists():
                return redirect('landing:sign_in')

            user_form.instance.username = email.lower()
            user = user_form.save()

            students_group = Group.objects.get(name='students')
            students_group.user_set.add(user)

            student_form.instance.user = user
            student_form.save()

            return redirect('registration:student_success')

        return render(request, 'registration/student_form.html', context={
            'user_form': user_form,
            'student_form': student_form,
        })


class StudentSuccessView(generic.TemplateView):
    template_name = 'registration/student_success.html'


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'registration/student_update.html'

    def get_object(self, queryset=None):
        return self.request.user.student


class StudentPasswordUpdateView(View):
    def get(self, request):
        form = PasswordChangeForm(self.request.user)

        return render(request, 'registration/student_password_update.html', context={
            'form': form,
        })

    def post(self, request):
        form = PasswordChangeForm(self.request.user, data=self.request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(self.request.user.student.get_absolute_url())

        return render(request, 'registration/student_password_update.html', context={
            'form': form,
        })


class TicketCreateView(generic.CreateView):
    model = Ticket
    form_class = TicketForm

    def form_valid(self, form):
        ret = super().form_valid(form)

        if not settings.DEBUG:
            EmailMessage('Ticket de Registro de LabMat', 'Ticket: ' + self.object.secret, to=[self.object.email]).send()

        return ret


class TicketDetailView(generic.DetailView):
    model = Ticket

    def is_debug(self):
        return settings.DEBUG
