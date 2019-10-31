from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user :
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('jobs_list'))
                else:
                    return HttpResponse('user is not active')
            else:
                return HttpResponse('user is none')
    else:
        form = UserLoginForm()

    context = {
        'form':form ,
    }
    return render(request, 'accounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('jobs_list')


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user = new_user)
            return redirect('jobs_list')
    else:
        form = UserRegistrationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST or None, instance = request.user)
        profile_form = ProfileEditForm(request.POST or None, instance = request.user.profile, files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit_profile')
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/edit_profile.html', context)
