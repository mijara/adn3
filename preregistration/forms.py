from django import forms
from .models import *


class PreRegistrationForm(forms.ModelForm):
    class Meta:
        model = PreRegistration

        fields = [
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
