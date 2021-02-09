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

    def __str__(self):
        return '%s-%s-%s-%s-%s-%s'%(self.firstname,self.lastname,self.email,self.subscription_date,self.end_subscription_date,self.active)
    class Meta:
        unique_together = (('firstname', 'lastname','email'),)

class Event(models.Model):
    name=models.CharField(max_length=120)
    url=models.URLField()
    creation_date=models.DateField()
    place_name=models.CharField(max_length=120)
    place_address=models.CharField(max_length=120)
    place_city=models.CharField(max_length=120)
    place_zipcode=models.CharField(max_length=120)
    place_country=models.CharField(max_length=120)

    def __str__(self):
        return '%s' % (self.name)
    class Meta:
        unique_together = (('url',),)