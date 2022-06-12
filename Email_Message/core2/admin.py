from django.contrib import admin
from core2.models import Email

# Register your models here.
@admin.register(Email)
class SignupTBModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password','date_time')