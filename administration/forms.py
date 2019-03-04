from django import forms
from django.contrib.auth.models import User

from adn3.services import get_period_year
from courses.models import Course, Campus, Agenda
from courses.services import get_active_courses


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
    teacher = forms.ModelChoiceField(queryset=None, label="Profesor(a)",
                                     widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))

    course = forms.ModelChoiceField(queryset=None, label="Curso",
                                    widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))

    def __init__(self, *args, **kwargs):
        super(TeacherCourseForm, self).__init__(*args, **kwargs)

        self.fields['teacher'].queryset = User.objects.filter(groups__name="teachers")

        self.fields['course'].queryset = get_active_courses()


class CoAssistantCourseForm(forms.Form):
    assistant = forms.ModelChoiceField(queryset=None, label="Ayudante",
                                       widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))

    course = forms.ModelChoiceField(queryset=None, label="Curso",
                                    widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))

    def __init__(self, *args, **kwargs):
        super(CoAssistantCourseForm, self).__init__(*args, **kwargs)

        self.fields['assistant'].queryset = User.objects.filter(groups__name="assistants")

        self.fields['course'].queryset = get_active_courses()


class SelectCourseForm(forms.Form):
    course = forms.ModelChoiceField(queryset=None, label="Curso",
                                    widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))

    def __init__(self, *args, **kwargs):
        super(SelectCourseForm, self).__init__(*args, **kwargs)

        self.fields['course'].queryset = get_active_courses()


class AssistantAgendaForm(forms.Form):
    agenda = forms.ModelChoiceField(queryset=None, label="Agenda",
                                    widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))

    assistant = forms.ModelChoiceField(queryset=None, label="Ayudante",
                                       widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))

    def __init__(self, *args, **kwargs):
        super(AssistantAgendaForm, self).__init__(*args, **kwargs)

        course_pk = kwargs.pop('course_pk', None)

        self.fields['agenda'].queryset = Agenda.objects.filter(course__pk=course_pk)

        self.fields['assistant'].queryset = User.objects.filter(groups__name="assistants")


class AssistantForm(forms.Form):
    student = forms.ModelChoiceField(queryset=None, label="Estudiante",
                                     widget=forms.Select(attrs={'class': 'selectpicker', 'data-live-search': 'true'}))

    def __init__(self, *args, **kwargs):
        super(AssistantForm, self).__init__(*args, **kwargs)

        self.fields['student'].queryset = User.objects.filter(groups__name="students")


class AgendaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = get_active_courses()

    class Meta:
        model = Agenda
        fields = ('day', 'block', 'room', 'course')
