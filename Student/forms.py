from django import forms
from .models import Student_model,Grade
from courses.models import Course_models

class Student_Forms(forms.ModelForm):
    class Meta:
        model = Student_model
        fields = ['Student_name']
        courses = forms.ModelMultipleChoiceField(queryset=Course_models.objects.all(), widget = forms.CheckboxSelectMultiple)


class AssignGradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student','course','grade']
        widgets = {
              'grade': forms.TextInput(attrs = {'palceholder':'Enter Grade (e.g. A,B,C)'})
        }
