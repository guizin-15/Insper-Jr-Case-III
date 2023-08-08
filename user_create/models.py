from django.contrib.auth.models import User #User is djangos original user model, will be using it as base to other user fields were gonna add without losing the autentication functions (which could happen on the use of abstract user)
from django.db import models

# Create your models here.

#1 to 1 Profile model which will be added to our users, allowing us to add fields to each user without the use of Abstract Users
class Profile(models.Model):

    #Especify the model as beign a One to One with the object(User)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    #Declaration of every Tuple of choices that the user will have to complete:
    Genders = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro'),
    )

    #User type, will not be displayed for the users at any given moment, will only be displayed to Admin and is only usable for back-end coding
    User_types = (
        ('Usuario', 'Usuario'),
        ('Funcionario', 'Funcionario'),
        ('Administrador', 'Administrado'),
    )


    #Here we set every element of the Profile model, starting by the admin/backend oriented ones
    user_type = models.CharField(max_length=100, choices=User_types, blank=True, null=True, verbose_name='Tipo Usuario')
    
    #Will set again the very same elements of the original django profile for convenience purpouses, facilitanting the DB view
    first_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Nome')
    last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Sobrenome')
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='E-mail') 

    #Other fields
    nickname = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nome de exibição')

    #Profile img needs a place to be uploaded to, correction pendent
    # profile_img = models.ImageField(upload_to='WAITING FOR FILL', blank=True, null=True, verbose_name='Foto de Perfil')

    birth = models.DateField(null=True, blank=True, verbose_name='Data de nascimento')
    phone_number = models.CharField(max_length=19, null=True, blank=True, verbose_name='Número de Telefone')
    gender = models.CharField(max_length=20, choices=Genders, null=True, blank=True, verbose_name='Gênero')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_acces = models.DateTimeField(auto_now=True)