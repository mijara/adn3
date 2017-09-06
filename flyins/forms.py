from django import forms
from .models import *
from django.core.exceptions import ValidationError


class FlyInForm(forms.ModelForm):
    class Meta:
        model = FlyIn

        fields = [
            'first_name',
            'last_names',
            'rol',
            'usm_priority',
            'course',
            'first_preference',
            'second_preference',
            'third_preference',
            'fourth_preference',
            'fifth_preference',
            'parallel',
            'software',
            'previous_experience',
        ]


class RolForm(forms.Form):
    rol = forms.CharField(max_length=11)

    def clean_rol(self):
        rol = self.cleaned_data['rol']

        split_rol = rol.split('-')

        if len(split_rol) < 2:
            raise ValidationError("Rol not valid")
        check_digit = split_rol[1]

        reversed_rol = split_rol[0][::-1]
        mult = [2,3,4,5,6,7]

        sum = 0

        for i, n in enumerate(reversed_rol):
            sum = sum + int(n) * mult[i % 6]

        digit = 11 - (sum % 11)

        if digit == 11:
            digit = 0
        elif digit == 10:
            digit = 'K'
        print(digit, check_digit)
        if check_digit.lower() != str(digit).lower():
            raise ValidationError("Rol not valid")

        return rol
