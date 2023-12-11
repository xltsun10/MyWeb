from django.urls import path 
from . import  views
urlpatterns = [
    path("", views.home ),
    path("home", views.home, name= "home"),
    path("detail", views.detail, name= "detail"),
    path("order", views.order,name="order"  ),
    path("checkout", views.checkout ,name="checkout" ), 
    path("update_item", views.updateItem , name="update_item"),   
    path("login", views.loginPage, name= "login"),
    path("logout", views.logoutPage, name= "logout"),
    path("register", views.register, name= "register"),
    path("search", views.search, name= "search"),
    path("category", views.category, name= "category"),
    path("sales", views.sales, name= "sales"),
]
