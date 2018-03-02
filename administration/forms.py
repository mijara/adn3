from django import forms
from django.contrib.auth.models import User

from courses.models import Course


class TeacherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'code', 'campus', 'year', 'semester', 'software')
