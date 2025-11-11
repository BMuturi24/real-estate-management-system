from django.shortcuts import render
from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer


# API Views
class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

# Home page render
def home(request):
      listings = [
        {'title': 'Apartment Downtown', 'price': 'KES 12,000', 'status': 'Rent'},
        {'title': 'House in Karen', 'price': 'KES 18,000,000', 'status': 'Sale'},
    ]
      return render(request, 'listings/home.html', {'listings': listings})
