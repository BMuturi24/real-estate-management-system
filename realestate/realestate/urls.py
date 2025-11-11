from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Your apps
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('enquiries/', include('enquiries.urls')),
    path('listings/', include('listings.urls')),
    path('properties/', include('properties.urls')),
    path('', include('core.urls')),  
]
