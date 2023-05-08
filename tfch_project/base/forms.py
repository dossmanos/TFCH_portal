"""This file contains all forms"""

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Pianist, Program, Concert



class MyUserCreationForm(UserCreationForm):
    """A user creation form"""
    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2"]


class UserForm(ModelForm):
    """A user form"""
    class Meta:
        model = Pianist
        fields = ["avatar"]

class ProgramForm(ModelForm):
    """A program form"""
    class Meta:
        model = Program
        fields = ["name", "program_pianist"]


class ConcertForm(ModelForm):
    """A concert form"""
    class Meta:
        model = Concert
        fields = "__all__"


class ProgramModificationForm(ModelForm):
    """A program modification form"""
    class Meta:
        model = Program
        fields = ["name", "program_pianist"]
