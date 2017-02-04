from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SignUp(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=512,unique=True)
    firstname=models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=0)
    otp = models.CharField(max_length=6 ,default=1234)
    #max_length=255,unique=True
    date_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return (self.firstname+" "+self.lastname)

