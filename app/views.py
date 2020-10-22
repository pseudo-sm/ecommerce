from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
# Create your views here.


@login_required(login_url="signin")
def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{"products":products})

def products(request):
    if request.GET.get("price") is None:
        products = list(Product.objects.all().values())
    else:
        products = list(Product.objects.filter(price__gte=request.GET.get("price")).values())
    return JsonResponse(products,safe=False)


def new_prdouct(request):
    return render(request,"new-product.html")

def new_product_action(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    new_product = Product(name=name,price=price,description=description)
    new_product.save()
    return redirect("/")


def signup(request):

    return render(request,"signup.html")

def signin(request):

    return render(request,"signin.html")

def signup_action(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    user = User.objects.create(username=username,password=password)
    new_customer = Customer(username=username,password=password,user_id=user)
    new_customer.save()
    return JsonResponse(True,safe=False)

def signin_action(request):
    username = request.GET.get("username")
    password = request.GET.get("password")

    users = User.objects.filter(username=username,password=password)
    if len(users) > 0:
        user = users.first()
        auth.login(request,user)
        print(user)
        customer = Customer.objects.get(user_id=user)
        return JsonResponse({"customer":customer.user_id.pk,"status":True},safe=False)
    else:
        return JsonResponse({"status":False})

def logout(request):
    auth.logout(request)
    return redirect("/signin")

