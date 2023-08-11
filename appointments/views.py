from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def appointments(request):
    return render(request, 'appointments.html')

def schedule(request): 
    return render(request, 'schedule.html')