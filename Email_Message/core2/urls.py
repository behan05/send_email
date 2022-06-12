from django.urls import path
from core2 import views

urlpatterns = [
    path('email/',views.email,name='email')
]