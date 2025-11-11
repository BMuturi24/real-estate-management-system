from django.shortcuts import redirect, render

def enquiries_home(request):
    return render(request, "enquiries/home.html")

def send_enquiry(request):
    if request.method == 'POST':
        # normally save to database here
        return redirect('enquiries:thank_you')
    return render(request, 'enquiries/form.html')

def thank_you(request):
    return render(request, 'enquiries/thank_you.html')