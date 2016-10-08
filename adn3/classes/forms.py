from django import forms
from models import *
from django.forms.extras import widgets


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('name', 'number', 'start_date', 'end_date')

        widgets = {
            'start_date': widgets.SelectDateWidget(),
            'end_date': widgets.SelectDateWidget(),
        }
