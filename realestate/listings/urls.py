from django.urls import path
from .views import ListingListCreateView, ListingDetailView, home

app_name = 'listings'

urlpatterns = [
    path('', home, name='listings_home'),  # Home page
    path('list/', ListingListCreateView.as_view(), name='listing_list_create'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing_detail'),
]
