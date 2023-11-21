from django.db import models

# Create your models here.
class DisneylandReview(models.Model):
    Review_ID = models.CharField(max_length=10)
    Rating = models.IntegerField()
    Year = models.CharField(max_length=10)
    Text = models.CharField(max_length=1000)
    Branch = models.CharField(max_length=255)


