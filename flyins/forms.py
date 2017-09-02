from django import forms
from .models import *


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
