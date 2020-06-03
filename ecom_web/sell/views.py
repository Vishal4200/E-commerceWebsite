from django.shortcuts import render,redirect,get_object_or_404
from sell.forms import FurnitureForm
from sell.models import Furniture,NewFurnitures
from cart.models import Cart

# Create your views here.

def sell(request):    
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()        
            return redirect("home")
        
    else:  
        form = FurnitureForm()
        return render(request,'sellpage.html', {'form' : form})

def homepage(request):
    post = Furniture.objects.all()
    query=request.GET.get('q')
    if query:
        post=Furniture.objects.filter(title__icontains=query)
    return render(request,'home.html',{'post' : post})

def newpage(request):
    post = NewFurnitures.objects.all()
    return render(request,'NewPost.html',{'post' : post})

def detail(request,old_product_slug ):
    post = get_object_or_404(Furniture, slug=old_product_slug)
    return render(request,'oldpost_detail.html',{'post' : post})

def newdetail(request,product_slug ):
    post = get_object_or_404(NewFurnitures, slug=product_slug)
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    return render(request,'newpost_detail.html',{'post' : post,'cart':cart_obj})
