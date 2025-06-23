from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Simulate sending email (configure in production)
        print(f"Received contact from {name} ({email}): {message}")
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
