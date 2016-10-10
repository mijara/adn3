# coding=utf-8
from django import forms
from models import *
from django.forms.extras import widgets


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('name', 'number', 'start_date', 'end_date', 'session_type', 'state')

        widgets = {
            'start_date': widgets.SelectDateWidget(),
            'end_date': widgets.SelectDateWidget(),
        }

        help_texts = {
            'number': u'Número de sesión, por defecto es la primera disponible.'
        }


class SessionFileForm(forms.ModelForm):
    class Meta:
        model = SessionFile
        fields = ('name', 'file',)
