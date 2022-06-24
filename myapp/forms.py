

from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    '''
    Adds more fields to user creation form
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class UserUpdateForm(forms.ModelForm):
    '''
    Form to update user profile
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    '''
    Form to update user profile picture
    '''
    area = forms.ModelChoiceField(queryset=Area.objects.all())
    class Meta:
        model = Profile
        fields = ['user_bio','area','profile_pic']
        
class ProductUpload (forms.ModelForm):
    '''
    Form to upload products
    '''
    class Meta:
        model = Product
        fields = ['product_name','product_pic','product_description','price','area']