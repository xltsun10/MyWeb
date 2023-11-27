from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null= True, blank= False)
    name = models.CharField(null = True, max_length=200)
    email = models.CharField(null = True, max_length=200)
    def __str__(self):
       return self.name

class Book(models.Model):
    name = models.CharField(null = True, max_length=200)
    price = models.FloatField()
    activate= models.BooleanField(default = False, null = True, blank = False)
    image=models.ImageField(null= True, blank= True, upload_to=None, height_field=None, width_field=None, max_length=None)
   
    def __str__(self):
       return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null= True)
    date = models.TimeField(auto_now_add=True)
    complete = models.BooleanField(default= False, null= True, blank= False)
    transaction_id= models.CharField(max_length=200, null = True)
    def __str__(self): 
        return self.id

class OrderItem(models.Model):
    book = models.ForeignKey(Book,  on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order,  on_delete=models.SET_NULL, null= True)
    quantity = models.IntegerField(default= 0, null= True, blank= True)
    date_added= models.DateTimeField(auto_now_add=False)

class Shipping(models.Model):
    customer = models.ForeignKey(Book,  on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order,  on_delete=models.SET_NULL, null= True)
    address= models.CharField(max_length=200, null= True)
    city= models.CharField(max_length=200, null= True)
    state= models.CharField(max_length=200, null= True)
    mobile= models.CharField(max_length=20, null= True)
    date_added= models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return self.address
    