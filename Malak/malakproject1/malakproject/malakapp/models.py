from random import choices
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Sign_Up(models.Model):
    username=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100, blank=True)
    Password = models.CharField(max_length=100)
    mobile = PhoneNumberField()
    country = CountryField()
    gender_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('Other','Other'),
    )
    gender =models.CharField(max_length=10,choices=gender_CHOICES)

    

    def __str__(self):
        return self.username


class Sign_in(models.Model):
    Email=models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Email

class Forgot_Password(models.Model):
    Email=models.EmailField(max_length=100)

    def __str__(self):
        return self.Email
