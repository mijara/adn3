from django import forms
from django.contrib.auth.models import User

from courses.models import Course, Agenda


class TeacherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'code', 'campus', 'year', 'semester', 'software')


class YearSemesterForm(forms.Form):
    year = forms.IntegerField(label='Año')

    semester = forms.ChoiceField(choices=(
        (1, 1),
        (2, 2)
    ), label='Semestre')


class TeacherCourseForm(forms.Form):
    teacher = forms.ModelChoiceField(queryset=User.objects.filter(groups__name="teachers"), label="Profesor(a)",
                                     widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Curso",
                                    widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))


class CoAssistantCourseForm(forms.Form):
    assistant = forms.ModelChoiceField(queryset=User.objects.filter(groups__name="assistants"), label="Ayudante",
                                       widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Curso",
                                    widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))
