from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nombres')
    last_name = forms.CharField(max_length=30, required=True, label='Apellidos')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('rol', 'campus')
        widgets = {
            'rol': forms.TextInput(attrs={'id': 'rol'}),
        }

    def clean_rol(self):
        rol = self.cleaned_data['rol']

        split_rol = rol.split('-')

        if len(split_rol) < 2:
            raise ValidationError("Rol not valid")
        check_digit = split_rol[1]

        reversed_rol = split_rol[0][::-1]
        mult = [2, 3, 4, 5, 6, 7]

        sum = 0

        for i, n in enumerate(reversed_rol):
            sum = sum + int(n) * mult[i % 6]

        digit = 11 - (sum % 11)

        if digit == 11:
            digit = 0
        elif digit == 10:
            digit = 'K'

        if check_digit.lower() != str(digit).lower():
            raise ValidationError(u'Rol inválido')

        return rol


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('usm_priority', 'campus')


class TicketForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Ya existe un usuario con este email')
        return email

    class Meta:
        model = Ticket
        fields = ('email',)
