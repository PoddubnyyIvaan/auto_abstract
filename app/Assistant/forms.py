from django import forms
from django.db import models
from .models import UserModel, EmailModel, OutModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["data_file"]
class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = ["user_email"]
        
class OutForm(forms.ModelForm):
    class Meta:
        model = OutModel
        fields = ['file_path']