from django.urls import path
from core3 import views

urlpatterns = [
    path('email_send/',views.email_send,name='email_send')
]