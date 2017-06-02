from django import forms
from .models import *


class PreRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PreRegistrationForm, self).__init__(*args, **kwargs)
        agendas = self.initial['course'].agenda_set

        self.fields['first_preference'].queryset = agendas
        self.fields['second_preference'].queryset = agendas
        self.fields['third_preference'].queryset = agendas

    class Meta:
        model = PreRegistration
        fields = [
            'first_preference',
            'second_preference',
            'third_preference'
        ]
