from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django_mysql.models import ListCharField
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Vendor(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    products = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    phone = PhoneNumberField()
    details = models.CharField(max_length=255)

    def __str__(self):
        return self.name