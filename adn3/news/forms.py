from django import forms
from models import *


class NewForm(forms.ModelForm):
    html = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = New
        fields = ('title', 'body', 'html', 'public')
        widgets = {
            'body': forms.Textarea(attrs={'style': 'display: none;'}),
        }

