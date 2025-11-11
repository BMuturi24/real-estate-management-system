from django.urls import path
from .views import properties_home

app_name = 'properties'

urlpatterns = [
    path('', properties_home, name='properties_home'),
]
