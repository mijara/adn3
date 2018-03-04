from django import forms
from django.contrib.auth.models import User

from courses.models import Course, Campus


class TeacherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(StudentForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['email'].label = 'Email'

    rol = forms.CharField(max_length=20, label='Rol USM')

    campus = forms.ModelChoiceField(queryset=Campus.objects.all())

    usm_priority = forms.IntegerField(label='Prioridad')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'code', 'campus', 'year', 'semester', 'software')
        help_texts = {
            'software': 'Mantenga la tecla <strong>control</strong> presionada para seleccionar más de uno.'
        }


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
