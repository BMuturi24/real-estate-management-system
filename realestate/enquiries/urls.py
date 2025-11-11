from django.urls import path
from . import views

app_name = 'enquiries'

urlpatterns = [
    path('', views.enquiries_home, name='home'),
    path('form/', views.send_enquiry, name='form'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
