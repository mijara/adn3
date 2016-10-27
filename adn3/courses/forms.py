from django import forms
from models import *


class CourseGradesConfigForm(forms.ModelForm):
    class Meta:
        model = CourseGradesConfig
        fields = ('grade_tests', 'grade_pretests', 'grade_assistance', 'show_final_grade')
