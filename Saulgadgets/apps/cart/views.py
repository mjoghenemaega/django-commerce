from django.conf import settings
from django.shortcuts import render, redirect
from django import forms
from . import forms

from .forms import PaymentForm
from django.contrib.auth.forms import UserCreationForm

from .cart import Cart
from django.conf import settings
from django.http import HttpResponse, HttpRequest


from .models import Payment


def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'], product.thumbnail.url, url, product.num_available)

        productsstring = productsstring + b

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        address = request.user.userprofile.address
        zipcode = request.user.userprofile.zipcode
        phone = request.user.userprofile.phone
    else:
        first_name = last_name = email = address = zipcode  = phone = ''

    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'zipcode': zipcode,
        
        'productsstring': productsstring.rstrip(',')
    }

    return render(request, 'cart.html', context)


def checkout(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        url = '/%s/%s/' % (product.category.slug, product.slug)
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'], product.thumbnail.url, url, product.num_available)

        productsstring = productsstring + b

    if request.method =="POST":
        payment_form= forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment =payment_form.save()
            return render(request,'checkout.html', {'payment' :payment})
    else:
            payment_form = forms.PaymentForm()
    return render (request, 'checkout.html', {'payment_form' : payment_form})        


def success(request):
    cart = Cart(request)
    cart.clear()
    
    return render(request, 'success.html')




