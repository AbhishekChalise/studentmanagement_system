from django import forms
from .models import Course_models

class Course_forms(forms.ModelForm):
    class Meta:
        model = Course_models
        fields = ['Course_name']
