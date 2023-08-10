from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from .models import Profile
from django import forms

#Creates the form used to creating a user using the standard UserCreationForm as base
class UserRegisterForm(UserCreationForm):
    #Placeholder for the form, filled automatically by the system
    user_type = forms.CharField(max_length=100, initial='', required=False, )
    age = forms.CharField(max_length=3, initial='', required=False)

    #Remaining fields of the model to be added to the form, in order
    first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'id': 'i1'}))
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'id': 'i2'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'id': 'i3'}))
    cpf = forms.CharField(max_length=14, required=True, widget=forms.TextInput(attrs={'id': 'i4'}))

    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={"id": "i5"}))
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={"id": "i6"}))
    
    profile_img = forms.ImageField(required=True)
    birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', "id": "i7"}), required=True,)
    phone_number = forms.CharField(max_length=19, required=True, widget=forms.TextInput(attrs={'id': 'i8'}))
    gender = forms.ChoiceField(choices=Profile.Genders, required=True, widget=forms.Select(attrs={'id': 'i9'}))

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
            'profile_img',
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
                profile_img = self.cleaned_data['profile_img'],
                birth = self.cleaned_data['birth'],
                phone_number = self.cleaned_data['phone_number'],
                gender = self.cleaned_data['gender'],
            )
        return user