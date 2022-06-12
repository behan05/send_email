from django.http import HttpResponse
from django.shortcuts import render
from core2.models import Email
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def email(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pwd = request.POST.get('password')
        db = Email(name=nm,email=em,password=pwd)
        db.save()
        sub = 'Welcome to our Website'
        message = 'hey {} Thanks for your Registration'.format(nm)
        send_from = settings.EMAIL_HOST_USER
        recipient = [em,'siteshsingh41@gmail.com']
        send_mail(sub,message,send_from,recipient)
        return HttpResponse(f'hey {nm} you are successfully Registered!!')
    
    return render(request,'signup.html')    
        
       
               
