from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import UserRegisterForm
from . import forms
from django.urls import reverse_lazy


# Create your views here.

class UserRegister(CreateView):
    form_class = UserRegisterForm #Defining the user creation form as the registration form we manually made at forms.py
    success_url = reverse_lazy('/') #Redirects the user after a succesfull signup

    def get_context_data(self, *args, **kwargs): #get_context_data method is remade to support the desired fields
        context = super().get_context_data(*args, **kwargs)
        context['first_name'] = self.request.POST.get('first_name')
        context['last_name'] = self.request.POST.get('last_name')
        context['email'] = self.request.POST.get('email')
        context['cpf'] = self.request.POST.get('cpf')
        context['username'] = self.request.POST.get('username')

        context['birth'] = self.request.POST.get('birth')
        context['phone_number'] = self.request.POST.get('phone_number')
        context['gender'] = self.request.POST.get('gender')

        return context
    


def signup(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.first_name + ' ' + user.last_name #Saves the username as first + last name
            user.save() 

            profile = user.profile
            age_delta = datetime.now().date() - profile.birth
            profile.age = age_delta.days // 365
            profile.user_type = 'Usuario' #Automatically creates the user as 'Usuario', employees shall be created using admin page
            profile.save()

            return redirect('/accounts/login/')  
    else:
        form = UserRegisterForm()
    return render(request, 'user_register.html', {'form': form})
