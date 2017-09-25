from django import forms
from courses.models import Agenda
from django.core.exceptions import ValidationError


class AgendaForm(forms.Form):
    code = forms.CharField(max_length=64, label='Código del curso',
                           widget=forms.TextInput(attrs={'id': 'code', 'autocomplete': 'off'}))

    course = forms.CharField(max_length=64, required=False, label='Curso',
                             widget=forms.TextInput(attrs={'id': 'course', 'readonly': 'true'}))

    agenda = forms.CharField(max_length=64, required=False, label='Horario',
                             widget=forms.TextInput(attrs={'id': 'agenda', 'readonly': 'true'}))
    agenda_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id': 'agenda-id'}))

    def clean(self):
        code = self.cleaned_data['code']
        agenda_id = self.cleaned_data['agenda_id']

        agenda = Agenda.objects.filter(pk=agenda_id, code=code)
        print(agenda)

        if agenda:
            return self.cleaned_data
        else:
            raise ValidationError("Rol not valid")
