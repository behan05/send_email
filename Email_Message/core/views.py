from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from core.models import SignupTB
from django.core.mail import send_mail

# Create your views here.
def signup(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pwd = request.POST.get('password')
        SignupTB(name=nm,email=em,password=pwd).save()
        subject = 'Welcome to our Website'
        message = f'hey {nm} Thank you for your interest in this website'
        send_from = settings.EMAIL_HOST_USER
        recipient =[em]
        send_mail(subject,message,send_from,recipient,fail_silently=False)
        return HttpResponse("you have got successfully mail!")
        
        
    return render(request,'signup.html',{'title':'SIGN UP'})
