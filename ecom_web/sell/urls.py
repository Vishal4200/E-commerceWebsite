from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='home'),
    path('new', views.newpage, name='new'),
    path('sell', views.sell, name='sell'),
    path('<slug:old_product_slug>/', views.detail, name='detail'), 
    path('new/<slug:product_slug>/', views.newdetail, name='newdetail'),
]