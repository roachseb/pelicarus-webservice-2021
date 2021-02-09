from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=22)
    subscription_date = models.DateField()
    end_subscription_date = models.DateField()
    active = models.BooleanField()