from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from .models import Profile
from django import forms

#Creates the form used to creating a user using the standard UserCreationForm as base
class UserRegisterForm(UserCreationForm):
    #Placeholder for the form, filled automatically by the system
    user_type = forms.CharField(max_length=100, initial='', required=False)
    age = forms.CharField(max_length=3, initial='', required=False)

    #Remaining fields of the model to be added to the form, in order
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)
    cpf = forms.CharField(max_length=14, required=True)

    #Profile IMG field, waiting for implementation
    # profile_img = forms.ImageField(required=True)

    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    phone_number = forms.CharField(max_length=19, required=True)
    gender = forms.ChoiceField(choices=Profile.Genders, required=True)

    #Meta declaration
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'cpf',
            'password1',
            'password2',
            'birth',
            'phone_number',
            'gender',
        ]

    #Function for saving the user together with the profile, 1 to 1
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False) #Uses the UserCreationForm save method
        #Save every info from the form
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save() #Saves the user

            Profile.objects.create(
                user = user,
                email = user.email,
                cpf = self.cleaned_data['cpf'],
                first_name = self.cleaned_data['first_name'],
                last_name = self.cleaned_data['last_name'],
                birth = self.cleaned_data['birth'],
                phone_number = self.cleaned_data['phone_number'],
                gender = self.cleaned_data['gender'],
            )
        return user