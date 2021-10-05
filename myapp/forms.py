from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from django import forms


class loginForm(AuthenticationForm):
  username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
  password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  model = User

  

class signupform(UserCreationForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

  class Meta:
    model = User
    fields = ['username']
    widgets = {
      'username':forms.TextInput(attrs={'class':'form-control'}),
    }

