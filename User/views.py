from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,CreateUserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
user = User.objects.first()  # or replace with a specific user
# profile = user.profile
# print(profile.image.url)
# print(profile.phone)

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f"Account Successfully Created - {user}")
            return redirect('user-login')
    else:
        form = CreateUserForm()
        
        
    context = {
        'form':form,
        
    }
    return render(request,'user/register.html',context)
@login_required
def profile(request):
    context = {
        'user':request.user,
        
    }
    return render(request,'user/profile.html',context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_update = CreateUserUpdateForm(request.POST,instance=request.user)
        user_profile_update = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if user_update.is_valid() and user_profile_update.is_valid():
            user_update.save()
            user_profile_update.save()
            return redirect('dashboard-profile')
    else:
        user_update = CreateUserForm(instance=request.user)
        user_profile_update = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_update':user_update,
        'profile_update_form': user_profile_update,  
    }
    return render(request,'user/profile_update.html',context)
