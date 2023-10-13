from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields=['title','doe','num_copies']
        



