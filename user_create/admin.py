from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from django.contrib import admin

class ProfileInline(admin.StackedInline): #A class that permits the display of the profile together with its origin user
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,) # Makes it so the profile is show together with the user, inline

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
