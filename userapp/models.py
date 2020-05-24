from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    pwd = models.CharField(max_length=10)
