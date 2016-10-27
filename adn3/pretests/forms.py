from django import forms
from models import *


class PretestForm(forms.ModelForm):
    class Meta:
        model = Pretest
        fields = ('name', 'start_session', 'end_session', 'percentage', 'show_grade')


class PretestFileForm(forms.ModelForm):
    class Meta:
        model = PretestFile
        fields = ('name', 'file')
