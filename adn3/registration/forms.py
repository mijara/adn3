from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nombres')
    last_name = forms.CharField(max_length=30, required=True, label='Apellidos')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class StudentForm(forms.ModelForm):
    secret = forms.CharField(max_length=64, label='Código')

    class Meta:
        model = Student
        fields = ('rol', 'usm_priority', 'campus')


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('usm_priority', 'campus')


class TicketForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe un usuario con este email')
        return email

    class Meta:
        model = Ticket
        fields = ('email',)
