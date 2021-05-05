from django.db import models

# Create your models here.

# class Details(models.Model):
#     name = models.CharField(max_length=50,default='',null=False)
#     email = models.CharField(max_length=50,default='',null=False)
#     phno = models.CharField(max_length=13,default='',null=False)

class Details(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phno = models.CharField(max_length=10)