from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Cart, Item
from product.models import Product
from django.http import JsonResponse
import json
# Create your views here.

def cart(request):
    try:
        cart = Cart.objects.get(user = request.user)
        items = cart.item_set.all()
        print(int(items.count()), items)
        if int(items.count()) < 1:
            items = "its EMPTY"
        context = {
            'items': items
        }
    except:
        cart = Cart.objects.create(user = request.user)
        context = {
            "items": "its EMPTY"
        }
    
    return render(request, "cart/cart.html", context)

def add_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(productId, action)
    try:
        cart = Cart.objects.get(user = request.user)
        print("cart exists")
        try:
            cart_item = Item.objects.get(cart = cart, item = Product.objects.get(id = productId))
            cart_item.quantity += 1
            cart_item.total = cart_item.quantity * cart_item.item.price
            cart_item.save()
            print("Item exists and inc by 1", cart_item.quantity)
            return JsonResponse(str(cart_item.quantity), safe = False)
        except:
            cart_item = Item.objects.create(cart = cart, item = Product.objects.get(id = productId))
            cart_item.total = cart_item.quantity * cart_item.item.price
            cart_item.save()
            print("new item created")
    except:
        cart = Cart.objects.create(user = request.user)
        cart_item = Item.objects.create(cart = cart, item = Product.objects.get(id = productId))
        cart_item.total = cart_item.quantity * cart_item.item.price
        cart_item.save()
        print("Cart and item both created")
    print("last point boi")
    return JsonResponse("added to cart", safe = False)


def remove_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(productId, action)

    cart = Cart.objects.get(user = request.user)
    print("cart exists")
    try:
        cart_item = Item.objects.get(cart = cart, item = Product.objects.get(id = productId))
        if cart_item.quantity > 0:
            cart_item.quantity -= 1
            cart_item.total = cart_item.quantity * cart_item.item.price
            cart_item.save()
            print("Item exists and dec by 1", cart_item.quantity)
        return JsonResponse(str(cart_item.quantity), safe = False)
    except:
        cart_item = Item.objects.create(cart = cart, item = Product.objects.get(id = productId))
        cart_item.total = cart_item.quantity * cart_item.item.price
        cart_item.save()
        print("new item created")

    return JsonResponse("Item is removed", safe = False)


def clear_cart(request):
    print(request.user)
    cart = request.user.cart_set.first()
    cart.delete()
    return redirect("home")