from django.shortcuts import render

def properties_home(request):
    properties = [
        {'name': 'Luxury Villa', 'price': 'KES 15,000,000', 'type': 'Sale'},
        {'name': 'Studio Apartment', 'price': 'KES 25,000', 'type': 'Rent'},
    ]
    return render(request, 'properties/home.html', {'properties': properties})

