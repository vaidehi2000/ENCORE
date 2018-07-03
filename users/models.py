from django.db import models

class user(models.Model):
    name=models.CharField(max_length=100)
    rollnumber=models.IntegerField()
    branch=models.CharField(max_length=100)


# Create your models here.
