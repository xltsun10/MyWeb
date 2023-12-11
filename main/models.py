from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','first_name','last_name','password1','password2']
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null= True, blank= False)
    name = models.CharField(null = True, max_length=200)
    email = models.CharField(null = True, max_length=200)
    def __str__(self):
       return self.name
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    is_sub= models.BooleanField(default=False)
    name= models.CharField(max_length=200, null= True)
    slug= models.SlugField(max_length=200, unique= True)
    def __str__(self):
        return self.name
    

class Sale(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
class Book(models.Model):
    name = models.CharField(null = True, max_length=200)
    category= models.ManyToManyField(Category, related_name='book')
    author = models.CharField(null = True, max_length=100)
    price = models.FloatField()
    detail= models.TextField(null = True, blank=True)
    activate= models.BooleanField(default = False, null = True, blank = False)
    image=models.ImageField(null= True, blank= True, upload_to=None, height_field=None, width_field=None, max_length=None)
   
    def __str__(self):
       return self.name
    @property
    def ImageURL(self):
        try:
            url= self.image.url
        except:
            url=''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null= True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default= False, null= True, blank= False)
    transaction_id= models.CharField(max_length=200, null = True)
    def __str__(self): 
        return str(self.id)
    @property 
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    @property 
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total

class OrderItem(models.Model):
    book = models.ForeignKey(Book,  on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order,  on_delete=models.SET_NULL, null= True)
    quantity = models.IntegerField(default= 0, null= True, blank= True)
    date_added= models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total= self.book.price* self.quantity
        return total

class Shipping(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order,  on_delete=models.SET_NULL, null= True)
    address= models.CharField(max_length=200, null= True)
    city= models.CharField(max_length=200, null= True)
    state= models.CharField(max_length=200, null= True)
    mobile= models.CharField(max_length=20, null= True)
    date_added= models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return self.address
    
    