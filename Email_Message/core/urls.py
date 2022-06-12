from django.urls import path
from core import views


# create urls here.

urlpatterns = [
    path('signup/',views.signup,name="signup")
]