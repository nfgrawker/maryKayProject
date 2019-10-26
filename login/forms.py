from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=False)
    email = forms.EmailField()
    phone_number = forms.CharField(required=False)
    consultant_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','consultant_number', 'phone_number', 'email', 'password1', 'password2']
