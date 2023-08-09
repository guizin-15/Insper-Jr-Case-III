from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from . import forms


# Create your views here.
@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile


    if request.method == 'POST':
        #Keeps updating the user age, need to repeat this code through the program to alway keep it updated
        age_delta = datetime.now().date() - profile.birth
        profile.age = age_delta.days // 365

        form = forms.UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = user.first_name + ' ' + user.last_name
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            profile.email = form.cleaned_data['email']
            profile.phone_number = form.cleaned_data['phone_number']
            profile.gender = form.cleaned_data['gender']

            profile.save()
            user.save()
            return redirect('/accounts/profile/')



    else:
        #Set the initial values of the form as the user already setted values
        form = forms.UserEditForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': profile.email,
            'phone_number': profile.phone_number,
            'gender': profile.gender
        })


    return render(request, 'user_edit.html', {'form': form, 'user': user, 'profile': profile})

@login_required
def view_profile(request):
    user = request.user
    profile = user.profile

    return render(request, 'user_profile.html', {'user': user, 'profile': profile})

def custom_logout(request):
    logout(request)
    return redirect('/')