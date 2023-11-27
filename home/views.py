from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
   books= Book.objects.all()
   context= {'books': books}
   return render(request, 'pages/home.html', context)
def order(request):
   
   return render(request, 'pages/order.html')
def checkout(request):
   context={}
   return render(request, 'pages/checkout.html', context)