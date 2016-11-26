from django import forms
from models import *


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'session', 'software', 'timeout', 'show_grade', 'percentage']


class VersionFileForm(forms.Form):
    file = forms.FileField()


class ChoiceQuestionForm(forms.ModelForm):
    alternative_1 = forms.CharField(label='A)')
    alternative_2 = forms.CharField(label='B)')
    alternative_3 = forms.CharField(label='C)', required=False)
    alternative_4 = forms.CharField(label='D)', required=False)
    alternative_5 = forms.CharField(label='E)', required=False)

    correct = forms.IntegerField()

    class Meta:
        model = ChoiceQuestion
        fields = ['text', 'score', 'alternative_1', 'alternative_2', 'alternative_3', 'alternative_4', 'alternative_5']


class TextQuestionForm(forms.ModelForm):
    class Meta:
        model = TextQuestion
        fields = ['text', 'score']


class NumericalQuestionForm(forms.ModelForm):
    class Meta:
        model = NumericalQuestion
        fields = ['text', 'bottom_limit', 'top_limit', 'score']