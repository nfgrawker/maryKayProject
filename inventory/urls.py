from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.inventoryHome, name="inventoryHome"),
    path('addInventory/', views.addProduct, name="addProduct"),

]
