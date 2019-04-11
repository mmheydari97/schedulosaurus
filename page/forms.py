from django import forms
from .models import Task, User, Profile
from django.core import validators
from django.core.validators import RegexValidator


class PostForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title']


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class ProfileForm(forms.ModelForm):
    img = forms.ImageField(required=False)
    phone_regex = RegexValidator(regex=r'^\+?98?\d{9,15}$', message="Phone number up to 15 digits is allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17, required=False)

    class Meta:
        model = Profile
        exclude = ['user_id']