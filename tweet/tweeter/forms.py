from django import forms
from .models import Tweeter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweeterForm(forms.ModelForm):
    class Meta:
        model=Tweeter
        fields=['text','photo']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()

class Meta:
        model:User
        fields=('username','email','password1','password2')
