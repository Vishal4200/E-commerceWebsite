from . import views
from django.urls import path

urlpatterns = [
    path('checkout', views.checkout_page, name='checkout'),
    path('recipt', views.recipt, name='recipt'),
    path('handlerequest', views.handlerequest, name='handlerequest'),
]