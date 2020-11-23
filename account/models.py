from django.db import models
from django.contrib.auth.models import User
from django import forms
from django_resized import ResizedImageField


class Profile(models.Model):
    email = models.CharField(max_length=200, default="no e-mail...")
    bio = models.TextField(default='no bio')
    created = models.DateTimeField(auto_now_add=True)
    avatar = ResizedImageField(default='avatar.png',blank=True,size=[500,300],quality=75)
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    profile_name=models.CharField(max_length=100,default="no_name",blank=True)
    last_update = models.DateTimeField(null=True,blank= True)
    artilce_num = models.IntegerField(default=0)

    

    def __str__(self): 
        return f"{self.user}"
