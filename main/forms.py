from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Member

class Login_Form(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=20)
