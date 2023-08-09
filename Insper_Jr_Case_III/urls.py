"""
URL configuration for Insper_Jr_Case_III project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
#Here we use multiple url files for the same similar directories, because we cannot change the "accounts/" since we're using some of the django standard functions
#So instead we gotta make multiple files to compensate with our own without overlapping.
    path('accounts/logout/', include('user_edit.urls_logout')),
    path('accounts/profile/', include('user_edit.urls_profile')),
    path('accounts/edit/', include('user_edit.urls')),

    path('agendamentos/', include('appointments.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', include('user_create.urls')),
    path('', include('landing_page.urls')),
]
