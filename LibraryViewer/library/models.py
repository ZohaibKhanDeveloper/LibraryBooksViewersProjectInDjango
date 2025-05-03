from django.db import models

# Create your models here.
class Books_details(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    price = models.IntegerField()