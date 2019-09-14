from django import forms
from .models import *
from pretests.models import Pretest


class PretestGradeForm(forms.ModelForm):
    class Meta:
        model = Pretest
        fields = ('percentage', 'show_grade')


class CourseGradesConfigForm(forms.ModelForm):
    class Meta:
        model = CourseGradesConfig
        fields = ('grade_tests', 'grade_pretests', 'grade_assistance', 'show_final_grade')


class PasswordChangeTokenForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
