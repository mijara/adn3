from django import forms
from django.contrib.auth.models import User

from courses.models import Agenda
from .models import *


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('attended',)


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ('assistants', 'inscriptions')


class AgendaAddAssistantForm(forms.Form):
    assistant = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name="assistants"),
        label="Ayudante",
        widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'})
    )


class AgendaDeleteAssistantsForm(forms.Form):
    assistants = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        agenda_pk = kwargs.pop('agenda_pk', None)

        super().__init__(*args, **kwargs)

        assistants = [(a.pk, a) for a in Agenda.objects.get(pk=agenda_pk).assistants.all()]

        self.fields['assistants'].choices = assistants


class AgendaDeleteInscriptionsForm(forms.Form):
    inscriptions = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        agenda_pk = kwargs.pop('agenda_pk', None)

        super().__init__(*args, **kwargs)

        inscriptions = [(a.pk, a) for a in Agenda.objects.get(pk=agenda_pk).inscriptions.all()]

        self.fields['inscriptions'].choices = inscriptions


class AgendaAddInscriptionForm(forms.Form):
    inscription = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name="students"),
        label="Inscripción",
        widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'})
    )
