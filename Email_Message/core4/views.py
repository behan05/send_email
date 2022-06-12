from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from core4.models import Render_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.

def render_mail(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pwd = request.POST.get('password')
        TB = Render_mail(name=nm,email=em,password=pwd)
        TB.save()   
        
        subject = 'testing html email'
        recipient = [em]
        HTML_content = render_to_string('email_template.html',{"title":'RENDER EMAIL',"name":nm})
        text_content = strip_tags(HTML_content)
        email = EmailMultiAlternatives(
            subject,
            text_content,
            settings.EMAIL_HOST_USER,
            recipient
        )
        email.attach_alternative(HTML_content,'text/html')
        email.send()
        return HttpResponse('Thank You')

    return render(request,'render_mail.html')

