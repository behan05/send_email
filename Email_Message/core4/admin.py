from django.contrib import admin
from core4.models import Render_mail

# Register your models here.
@admin.register(Render_mail)
class SignupTBModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password','date_time')