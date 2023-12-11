from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def register(request):
   form = CreateUserForm()

   if request.method=="POST":
      form=CreateUserForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('login')
   context={'form':form}
   return render(request, 'app/register.html', context)

def loginPage(request):
   if request.user.is_authenticated:
      return redirect('home')
   if request.method== "POST":
      username=request.POST.get('username')
      password=request.POST.get('password')
      user= authenticate(request,username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('home')
      else: 
         messages.info(request, 'User or password is wrong')
   context={}
   return render(request, 'app/login.html', context)
def logoutPage(request):
   logout(request)
   return redirect('login')

def home(request):
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created =Order.objects.get_or_create(customer=customer, complete=False)
      items=order.orderitem_set.all()
      cartItems = order.get_cart_items
   else:
      items=[]
      order={'get_cart_items':0, 'get_cart_total':0}
      cartItems= order['get_cart_items']
   books= Book.objects.all()
   categories= Category.objects.filter(is_sub = False)
   active_category = request.GET.get('category','')
   context= {'categories':categories, 'books': books, 'cartItems':cartItems}
   return render(request, 'app/home.html', context)
def order(request):   
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created =Order.objects.get_or_create(customer=customer, complete=False)
      items = order.orderitem_set.all()
      cartItems = order.get_cart_items
   else:
      items=[]
      order={'get_cart_items':0, 'get_cart_total':0}
      cartItems= order['get_cart_items']
   context={'items':items, 'order':order, 'cartItems':cartItems}
   return render(request, 'app/order.html', context)
def checkout(request):
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created =Order.objects.get_or_create(customer=customer, complete=False)
      items=order.orderitem_set.all()
      cartItems = order.get_cart_items
   else:
      items=[]
      order={'get_cart_items':0, 'get_cart_total':0}
      cartItems= order['get_cart_items']
   context={'items':items, 'order':order, 'cartItems':cartItems}
   return render(request, 'app/checkout.html', context)
def updateItem(request):
   data = json.loads(request.body)
   bookId = data['bookId']
   action = data['action']
   
   print('Action', action)
   print('Book id', bookId)

   customer = request.user.customer
   book= Book.objects.get(id=bookId)
   order, created =Order.objects.get_or_create(customer=customer, complete=False)
   orderItem, created =OrderItem.objects.get_or_create(order=order, book= book)
   if action =='add':
      orderItem.quantity +=1
   elif action == 'remove':
      orderItem.quantity -= 1
   orderItem.save()
   if orderItem.quantity <= 0:
      orderItem.delete()

   return JsonResponse('Item was added in view', safe=False)

def search(request):
   if request.method=="POST":
      searched = request.POST["searched"]
      keys = Book.objects.filter(name__contains = searched)
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created =Order.objects.get_or_create(customer=customer, complete=False)
      items=order.orderitem_set.all()
      cartItems = order.get_cart_items
   else:
      items=[]
      order={'get_cart_items':0, 'get_cart_total':0}
      cartItems= order['get_cart_items']
   books= Book.objects.all()
   # context= {'books': books, 'cartItems':cartItems}
   return render (request, 'app/search.html',{"searched":searched,"keys":keys,'books': books, 'cartItems':cartItems})
def category(request):
   categories= Category.objects.filter(is_sub = False)
   active_category = request.GET.get('category','')
   if active_category:
      books = Book.objects.filter(category__slug = active_category)
   context={'categories':categories, 'books':books, 'active_category': active_category}
   return render(request, 'app/category.html', context)

def detail(request):   
   if request.user.is_authenticated:
      customer = request.user.customer
      order, created =Order.objects.get_or_create(customer=customer, complete=False)
      items = order.orderitem_set.all()
      cartItems = order.get_cart_items
   else:
      items=[]
      order={'get_cart_items':0, 'get_cart_total':0}
      cartItems= order['get_cart_items']

   id= request.GET.get('id','')
   books= Book.objects.filter(id=id)
   categories = Category.objects.filter(is_sub= False)
   context={'books':books,'categories':categories, 'items':items, 'order':order, 'cartItems':cartItems}
   return render(request, 'app/detail.html', context)
def sales(request):
    current_time = timezone.now()
    sale_items = Sale.objects.all()
    return render(request, 'app/detail.html', {'sale_items': sale_items})