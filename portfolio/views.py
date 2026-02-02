from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    succes = False
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        full_message = f"""
    
        New contact message from portfolio:
        
        Name: {name}
        Email: {email}
        
        Message:
        {message}
        """

        send_mail(
            subject="New Portfolio Contact Message",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        
        succes = True
    
    return render(request, 'portfolio/contact.html', {'success': succes})