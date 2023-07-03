from django.db import models

# Create your models here.

class storageUser(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    #email = models.CharField(max_length=100)
