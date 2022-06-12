from django.contrib import admin
from core.models import SignupTB

# Register your models here.

@admin.register(SignupTB)
class SignupTBModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password','date_time')
    
