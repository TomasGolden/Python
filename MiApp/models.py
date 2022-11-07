from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length = 40)
    lastName = models.CharField(max_length = 40)
    age = models.IntegerField()