from . import views
from django.urls import path

urlpatterns = [
    path('cart_home', views.cart_home, name='cart_home'),
    path('update', views.cart_update, name='update')
]