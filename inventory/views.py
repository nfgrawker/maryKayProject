from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Products, InventoryLog
# Create your views here.
def inventoryHome(request):
    context = {
        'products': Products.objects.all()
    }
    return HttpResponse("COMING SOON!")