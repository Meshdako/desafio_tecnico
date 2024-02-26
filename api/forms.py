from django import forms
from .models import *

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['input_word']