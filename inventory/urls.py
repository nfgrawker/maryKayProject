from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.inventoryHome, name="inventoryHome"),
    path("addInventory/", views.addProduct, name="addProduct"),
    path("changeForm/", views.orderForm, name="orderForm"),
    path("customerForm/", views.customerPage, name="customerForm"),
    path("submitCustomer/", views.submitCustomer, name="submitCustomer"),
]
