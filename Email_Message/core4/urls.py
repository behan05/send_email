from django.urls import path
from core4 import views

# create urls here.

urlpatterns =[
    path('render/',views.render_mail,name='render_mail')
]