from djongo import models

# Create your models here.
class Register(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=100)