#we need to modify the user and the from for create user 
from django.contrib.auth.models import User
from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile



class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        
        
#user from update 
class CreateUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

#also the user profile is update 
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','phone','image']
        
        
        
