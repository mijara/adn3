from django import forms

from classes.models import Session
from .models import *


class PretestForm(forms.ModelForm):
    class Meta:
        model = Pretest
        fields = ('name', 'start_session', 'end_session', 'percentage', 'show_grade', 'online')


class PretestFileForm(forms.ModelForm):
    class Meta:
        model = PretestFile
        fields = ('name', 'file')


class PretestUploadForm(forms.ModelForm):
    class Meta:
        model = PretestUpload
        fields = ('software', 'file')
