from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from user_create.models import Profile
from django import forms

#Just as the user creation form, well custom the django origin form to support the desired fields
class UserEditForm(UserChangeForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=100, required=True)

    phone_number = forms.CharField(max_length=19, required=True)
    gender = forms.ChoiceField(choices=Profile.Genders, required=True)


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'gender',
        ]