from django import forms
from .models import *


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('attended',)
