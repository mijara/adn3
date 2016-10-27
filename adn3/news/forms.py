from django import forms
from models import *


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ('title', 'body', 'public')
