from django.db import models


class userInfo(models.Model):
    userName = models.CharField(max_length=100, null=False )
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    passWord = models.CharField(max_length=100, null=False)
    confirmpass = models.CharField(max_length=100, null=False)
    
    class Meta:
        # Define the field to be used for latest()
        get_latest_by = 'id'

class DisneylandReview(models.Model):
    review_id = models.CharField(max_length=10000)
    rating = models.IntegerField()
    text = models.CharField(max_length=1000)
    branch = models.CharField(max_length=255)
    