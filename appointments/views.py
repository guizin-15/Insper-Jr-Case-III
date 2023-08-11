from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def empl_appointments(request):
    user = request.user
    profile = user.profile
    img = profile.profile_img
    profile_img = "/" + str(img)

    return render(request, 'empl_appointments.html', {"profile_img": profile_img})

# Create your views here.
def appointments(request):
    user = request.user
    profile = user.profile
    img = profile.profile_img
    profile_img = "/" + str(img)

    return render(request, 'appointments.html', {"profile_img": profile_img})

def schedule(request): 
    return render(request, 'schedule.html')