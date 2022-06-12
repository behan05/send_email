from django.db import models

# Create your models here.
class Email(models.Model):
    subject = models.TextField(max_length=570)
    message = models.TextField(max_length=570)
    date_time = models.DateTimeField(auto_now_add=True)