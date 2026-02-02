from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class signupData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.IntegerField()
    psw=models.CharField(max_length=100)

class feedbackData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    feedback=models.CharField(max_length=500)
    
class BookingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    event_type=models.CharField(max_length=100)
    date=models.DateField()
    # guestsc=models.ImageField()
    guestsc = models.IntegerField()
    guestsv=models.IntegerField()
    guestsn=models.IntegerField()
    message=models.CharField(max_length=100)