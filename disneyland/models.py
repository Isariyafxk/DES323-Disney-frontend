from django.db import models

# Create your models here.
from django.db import models

class userInfo(models.Model):
    userName = models.CharField(max_length=100, null=False )
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    passWord = models.CharField(max_length=100, null=False)
    confirmpass = models.CharField(max_length=100, null=False)
    
    




