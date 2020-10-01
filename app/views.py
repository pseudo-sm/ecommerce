from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
# Create your views here.



def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{"products":products})

def new_prdouct(request):
    return render(request,"new-product.html")

def new_product_action(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    new_product = Product(name=name,price=price,description=description)
    new_product.save()
    return redirect("/")
