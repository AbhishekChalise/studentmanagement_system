from django import forms
from .models import Student_model
from courses.models import Course_models

class Student_Forms(forms.ModelForm):
    class Meta:
        model = Student_model
        fields = ['Student_name', 'course']
        courses = forms.ModelMultipleChoiceField(queryset=Course_models.objects.all(), widget = forms.CheckboxSelectMultiple)



