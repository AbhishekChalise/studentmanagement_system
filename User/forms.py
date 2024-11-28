from django import forms
from .models import User_Model
from django.contrib.auth.forms import UserCreationForm

class User_Form(UserCreationForm):
    class Meta:
        model = User_Model
        fields = ['username', 'email','birth_date','is_student', 'is_teacher','course1','profile_picture']

# UserCreationForm does not need the password it will automatically do so!!!!!!.

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget = forms.PasswordInput())
    new_password = forms.CharField(widget = forms.PasswordInput())
    confirm_password = forms.CharField(widget = forms.PasswordInput())

    