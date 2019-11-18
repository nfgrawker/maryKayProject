from djongo import models

from login.models import User


# Create your models here.
class Products(models.Model):
    _id = models.ObjectIdField()
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(blank=True, max_length=500)
    quantity = models.IntegerField()
    consultant = models.ForeignKey(User, on_delete=models.CASCADE)
    optional_description = models.CharField(max_length=100, blank=True)
    price = models.BigIntegerField(default=0)


class Customers(models.Model):
    _id = models.ObjectIdField()
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, default="None")
    number = models.CharField(max_length=15, default="Unknown")
    email = models.EmailField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=20)
    consultant = models.ForeignKey(User, on_delete=models.CASCADE)


class InventoryLog(models.Model):
    _id = models.ObjectIdField()
    type = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    consultant = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customers, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
