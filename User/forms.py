from django import forms
from .models import User_Model
from django.contrib.auth.forms import UserCreationForm

class User_Form(UserCreationForm):
    class Meta:
        model = User_Model
        fields = ['username', 'email', 'is_student', 'is_teacher','course1']

# UserCreationForm does not need the password it will automatically do so!!!!!!.

