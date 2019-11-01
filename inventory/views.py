from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Products, InventoryLog
from django.http import Http404
import json
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def inventoryHome(request):
    if request.user.is_authenticated:
        products = Products.objects.filter(consultant=request.user)
        for product in products:
            product.price = product.price/100
            product.price = format(product.price, '.2f')

        context = {
            'products': products
        }
        print(request.user)
        return render(request, "inventory/inventoryTables.html", {"products": products})

@login_required
def createProductsTest(request):
    print(request.POST)
    return HttpResponse("Success")

@login_required
def addProduct(request):
    if request.method == "POST":
        jsonIncoming = json.loads(request.body.decode('utf8'))
        print(jsonIncoming)
        product_name = jsonIncoming["name"]
        product_description = jsonIncoming["description"]
        price = int(jsonIncoming["price"].replace(".",""))
        quantity = jsonIncoming["quantity"]
        model = Products(product_name=product_name, quantity=quantity, price=price,
                         product_description=product_description, consultant=request.user)
        log = InventoryLog(type="add",consultant=request.user,quantity=quantity, price=price, product=model)
        model.save()
        log.save()
        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        raise Http404("Did not use post")
