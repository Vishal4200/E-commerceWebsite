from django.db import models
from sell.models import NewFurnitures
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save,m2m_changed
from django.conf import settings
# Create your models here.
  
class CartManager(models.Manager):
    def user_create(self,user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

    def new_or_get(self,request):
            cart_id = request.session.get("cart_id",None)
            qs = self.get_queryset().filter(id=cart_id)
            if qs.count() == 1:
                new_obj = False
                cart_obj  = qs.first()
                if request.user.is_authenticated and cart_obj.user is None:
                    cart_obj.user = request.user
                    cart_obj.save()
            else:
                cart_obj = Cart.objects.user_create(user=request.user)
                new_obj = True
                request.session['cart_id']=cart_obj.id
            return cart_obj, new_obj

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    products = models.ManyToManyField(NewFurnitures,blank=True)
    subtotal = models.DecimalField(default=0.00,max_digits=50, decimal_places=2)
    total = models.DecimalField(default=0.00,max_digits=50, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    class Meta:
        db_table="Cart"
    def __str__(self):
        return "Cart of user id {}".format(self.id)

def m2m_save_cart_reciver(sender,instance,action,*args,**kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        subtotal=0
        for x in products:
            subtotal += x.price
        instance.subtotal = subtotal
        instance.save()

m2m_changed.connect(m2m_save_cart_reciver,sender=Cart.products.through)

def pre_save_cart_reciver(sender,instance,*args,**kwargs):
    instance.total = instance.subtotal

pre_save.connect(pre_save_cart_reciver,sender=Cart)