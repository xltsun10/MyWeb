from django.urls import path 
from . import  views
urlpatterns = [
    path("", views.home ),
    path("home", views.home ),
    path("order", views.order,name="order"  ),
    path("checkout", views.checkout ,name="checkout" ), 
    path("update_item", views.updateItem , name="update_item"),   
]
