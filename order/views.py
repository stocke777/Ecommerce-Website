from django.shortcuts import redirect, render
from django.http import HttpResponse
from cart.models import Cart, Item
from users.models import Profile
from .forms import AddressForm
from .models import Order, OrderItem
from django.views.generic.list import ListView
from django.core.mail import EmailMessage
from django.views import View
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokengenerator import token_generator
from django.urls import reverse


# Create your views here.

def orders_list(request):
    order = Order.objects.get(user = request.user)
    context = {
        "item_list" : OrderItem.objects.filter(order = order)
    }
    return render(request, "order/orders.html", context)

def checkout(request):

    cart = Cart.objects.get(user = request.user)
    cart_items = Item.objects.filter(cart = cart)
    total_price = 0

    for item in cart_items:
        total_price += item.total

    context = {
        "total_price" : total_price,
        "cart_items" : cart_items
    }

    return render(request, "order/checkout.html", context)

def place_order(request):
    profile = Profile.objects.get(user = request.user)

    print(profile.firstname)
    context = {
        "profile" : profile,
    }
    return render(request, "order/place_order.html", context)


def address(request):
    profile = Profile.objects.get(user = request.user)
    print("PROFILE IS VERIFIED________", profile.verified)
    # VERIFICATION EMAIL
    if profile.verified == False:
        print("EMAIL HERE")

        uidb64 = urlsafe_base64_encode(force_bytes(request.user.pk))
        token = token_generator.make_token(request.user)

        domain = get_current_site(request).domain
        link = reverse('activate', kwargs = {
            'uidb64': uidb64,
            'token': token,
        })
        activate_url = "http://"+domain+link
        email_check = EmailMessage(
            "Hello",
            "Verify Email "+request.user.email+" at our site\n" + activate_url,
            "noreply@home.com",
            [request.user.email]
        )
        email_check.send(fail_silently=False)
        print("EMAIL S ENT")
        return redirect('cart')
    
    print("BYPASSED EMAIL")
    form = AddressForm()
    if request.method == "POST":
        print(request.POST['Address'])
        cart = Cart.objects.get(user = request.user)
        cart_items = Item.objects.filter(cart = cart)
        total_price = 0

        for item in cart_items:
            total_price += item.total

        profile = Profile.objects.get(user = request.user)
        if request.POST['Address'] == "Option 1":
            order = Order.objects.create(user = request.user, total = total_price, address = profile.address)
        else:
            order = Order.objects.create(user = request.user, total = total_price, address = profile.address2)

        for item in cart_items:
            order_item = OrderItem.objects.create(order = order, item = item.item, quantity = item.quantity)

        return redirect('order_success')

    context = {
        "form": form,
        "profile" : profile,
    }
    return render(request, "order/address.html", context)

def order_success(request):
    return render(request, "order/order_success.html")


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            print(id, "    ", request.user.id)
            if int(id) == request.user.id:
                request.user.profile.verified = True
                request.user.profile.save()
                print("user verified")
            else:
                print("doesnt match")
            return redirect('cart')
        except:
            return redirect('cart')