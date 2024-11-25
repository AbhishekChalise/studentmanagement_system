from django import forms
from .models import Teacher_models

class Teacher_forms(forms.ModelForm):
    class Meta:
        model = Teacher_models
        fields = ['Teacher_name'] 


