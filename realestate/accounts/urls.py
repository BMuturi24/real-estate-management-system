from django.urls import path
from .views import RegisterView, ProfileView, ObtainAuthTokenView, home, profile

app_name = 'accounts'

urlpatterns = [
   
    path('', home, name='accounts/home'),  # Home page
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api/token/', ObtainAuthTokenView.as_view(), name='token_obtain'),
    path('profile/', profile, name='profile'),
]
