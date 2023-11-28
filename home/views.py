from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
def updateItem(request):
   data = json.loads(request.body)
   bookId = data['bookId']
   action = data['action']
   customer = request.user.customer
   book= Book.objects.get(id= bookId)
   order, created =Order.objects.get_or_create(customer=customer, complete=False)
   orderItem, created =OrderItem.objects.get_or_create(order=order, book= book)
   if action =='add':
      orderItem.quantity +=1
   elif action == 'remove':
      orderItem.quantity-=1
   orderItem.save()
   if orderItem.quantity<=0:
      orderItem.delete()

   return JsonResponse('add', safe=False)
