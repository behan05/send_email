from django.conf import settings
from django.shortcuts import render,HttpResponse
from core3.models import Email
from django.core.mail import BadHeaderError, send_mail

# Create your views here.

def email_send(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Email(subject=subject,message=message).save()
        if subject and message:
            try:
                send_mail(subject,message,settings.EMAIL_HOST_USER,['vihan095678@gmail.com','behankrbth@gmail.com'])     
            except BadHeaderError:
                return HttpResponse('invalid Header Error!!')
            else:
                return HttpResponse('Your Forn Is Successfully Registered !!')    
            
    return render(request,'detail.html',{"title":'Send Mail'})        
        
