from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.patient_login, name='patient_login'),
    path('register/', views.patient_register, name='patient_register'),
    path('donarlogin/', views.donar_login, name='donar_login'),
    path('donarregister/', views.donar_register, name='donar_register'),
    path('base/', views.base, name='base'),
    path('base1/', views.base1, name='base1'),
    path('donate/', views.donate_blood, name='donate_blood'),
    path('history/', views.donation_history, name='donation_history'),
    path('request/', views.blood_request, name='blood_request'),
    path('history/', views.request_history, name='request_history'),


]
