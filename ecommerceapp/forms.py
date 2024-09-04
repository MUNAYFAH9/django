from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class LoginUserForm(AuthenticationForm):
    class Meta:
        modle=User
        fields=('username','password',)

