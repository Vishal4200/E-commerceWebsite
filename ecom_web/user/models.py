from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    Photo = models.ImageField(upload_to='Profiles/',null=True,blank=True,default='Profiles/default-user-img.jpg')

    def __str__(self):
        return "Profile of user {}".format(self.user.username)
