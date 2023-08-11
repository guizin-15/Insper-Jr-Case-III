from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointments, name='appointments'),
    path('funcionario/', views.empl_appointments, name='empl-appointments'),
    path('schedule/', views.schedule, name='schedule')
]