from django.urls import path 
from . import  views
urlpatterns = [
    path("", views.index ),
    path("home", views.index ),
    path("order", views.order,name="order"  ),
    path("checkout", views.checkout ,name="checkout" ), 
    path("update_item", views.updateItem , name="update_item"),   
]
