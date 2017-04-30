from django import forms
from models import *


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'session', 'software', 'timeout', 'show_grade', 'percentage']


class VersionFileForm(forms.Form):
    file = forms.FileField()


class ChoiceQuestionForm(forms.ModelForm):
    html = forms.CharField(widget=forms.HiddenInput())
    alternative_1 = forms.CharField(label='A)')
    alternative_2 = forms.CharField(label='B)')
    alternative_3 = forms.CharField(label='C)', required=False)
    alternative_4 = forms.CharField(label='D)', required=False)
    alternative_5 = forms.CharField(label='E)', required=False)

    correct = forms.IntegerField()

    class Meta:
        model = ChoiceQuestion
        fields = ['text', 'html', 'score', 'alternative_1', 'alternative_2', 'alternative_3', 'alternative_4', 'alternative_5']
        widgets = {
            'text': forms.Textarea(attrs={'style': 'display: none;'}),
        }

class TextQuestionForm(forms.ModelForm):
    html = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = TextQuestion
        fields = ['text', 'html', 'score']
        widgets = {
            'text': forms.Textarea(attrs={'style': 'display: none;'}),
        }


class NumericalQuestionForm(forms.ModelForm):
    html = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = NumericalQuestion
        fields = ['text', 'html', 'bottom_limit', 'top_limit', 'score']
        widgets = {
            'text': forms.Textarea(attrs={'style': 'display: none;'}),
        }