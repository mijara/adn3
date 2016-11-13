from django import forms
from models import *


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'session', 'software', 'timeout', 'show_grade', 'percentage']
