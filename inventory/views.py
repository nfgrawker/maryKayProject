import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Products, InventoryLog


# Create your views here.
@login_required
def inventoryHome(request):
    if request.user.is_authenticated:
        products = Products.objects.filter(consultant=request.user)
        for product in products:
            product.price = product.price / 100
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
        try:
            jsonIncoming = json.loads(request.body.decode('utf8'))
            print(jsonIncoming)
            product_name = jsonIncoming["name"]
            product_description = jsonIncoming["description"]
            price = int(jsonIncoming["price"].replace(".", ""))
            quantity = jsonIncoming["quantity"]
            model = Products(product_name=product_name, quantity=quantity, price=price,
                             product_description=product_description, consultant=request.user)
            log = InventoryLog(type="add", consultant=request.user, quantity=quantity, price=price, product=model)
            if not settings.DEBUG:
                model.save()
                log.save()
            messages.success(request, "Your inventory has been saved!")
            response = {'status': 1, 'message': ("Ok")}  # for ok
            return HttpResponse(json.dumps(response), content_type='application/json')
        except Exception as e:
            # TODO: add lOGGER
            pass

    else:
        raise Http404("Did not use post")
