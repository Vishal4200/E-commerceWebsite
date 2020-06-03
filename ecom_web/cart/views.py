from django.shortcuts import render,redirect
from sell.models import NewFurnitures
from .models import Cart
# Create your views here.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request,'cart_home.html',{'cart' : cart_obj})

def cart_update(request):
    product_id=  request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = NewFurnitures.objects.get(id=product_id)
        except:
            print("Show msg to user,Product doesn't exists.")
            return redirect("cart:cart_home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)     
        else:
            cart_obj.products.add(product_obj)    
    return redirect("cart:cart_home")