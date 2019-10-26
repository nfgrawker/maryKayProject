from django.db import models
from login.models import User
# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(blank=True,max_length=500)
    quantity = models.IntegerField()
    consultant = models.ForeignKey(User, on_delete=models.CASCADE)
    optional_description = models.CharField(max_length=100, blank=True)
    price = models.BigIntegerField(default=0)

class InventoryLog(models.Model):
    type = models.CharField(max_length=10)
    quantity = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    consultant = models.ForeignKey(User, on_delete=models.CASCADE)