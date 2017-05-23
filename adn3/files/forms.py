from django import forms
from .models import *


class CourseFileForm(forms.ModelForm):
    class Meta:
        model = CourseFile
        fields = ('name', 'file')
