from djongo import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    consultant_number = models.IntegerField(default=0000)
    class Meta:
        proxy = True
