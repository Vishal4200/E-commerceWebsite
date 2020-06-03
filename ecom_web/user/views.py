from django.shortcuts import render,redirect
from .models import Profile
from user.forms import UserLoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('sell:home'))
                else:
                    return HttpResponse('User is not active')
            else:
                return HttpResponse('Invalid User')
    else:
        form = UserLoginForm()
    return render(request,'login.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('sell:home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('sell:home')
    else:
        form = UserRegistrationForm()
    return render(request,'register.html', {'form' : form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data = request.POST or None , instance = request.user)
        profile_form = ProfileEditForm(data = request.POST or None , instance = request.user.profile, files = request.FILES or None)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)

    return render(request,'edit_profile.html',{'user_form' : user_form,'profile_form' : profile_form})