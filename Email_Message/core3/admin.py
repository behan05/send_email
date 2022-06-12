from django.contrib import admin
from core3.models import Email

# Register your models here.
@admin.register(Email)
class SignupTBModelAdmin(admin.ModelAdmin):
    list_display = ('id','subject','message','date_time')