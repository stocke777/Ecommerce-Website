from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from product.models import Category, Product
from django.views.generic.list import ListView
# Create your views here.

def home(request):
    
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request, "front/home.html", context)


def productlist(request, pk):
    products = Product.objects.filter(category = pk)
    context = {
        'products':products,
    }
    return render(request, "front/list.html", context)


def product_details(request, pk):
    
    product = Product.objects.get(id = pk)
    images = product.product_images.all()
    print(product, images)
    context = {
        'product':product,
        'images':images,
    }
    return render(request, "front/product_details.html", context)