from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
   books= Book.objects.all()
   context= {'books': books}
   return render(request, 'pages/home.html', context)
def order(request):   
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created =Order.objects.get_or_create(customer=customer, complete=False)
      items=order.orderitem_set.all()
   else:
      items=[]
      order={'get_cart_items':0, 'get_cart_total':0}
   context={'items':items, 'order':order}
   return render(request, 'pages/order.html', context)
def checkout(request):
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created =Order.objects.get_or_create(customer=customer, complete=False)
      items=order.orderitem_set.all()
   else:
      items=[]
      order={'get_cart_items':0, 'get_cart_total':0}
   context={'items':items, 'order':order}
   return render(request, 'pages/checkout.html', context)