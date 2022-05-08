from django import forms
from django.forms import ModelForm
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']