from django.db import models
from cart.models import Cart
from django.contrib.auth.models import User
from payment.utils import unique_order_id_generator
from django.db.models.signals import pre_save
from django.utils import timezone
# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=120 , blank=True)
    name = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=30)
    #cart = models.ForeignKey(Cart,on_delete=models.CASCADE)

    class Meta:
        db_table="Order_Details"

    def __str__(self):
        return self.name + ' - ' + self.order_id

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id= unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)

class pay(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name='rel_payment_paytm',default=None)
    MID = models.CharField(max_length=40)
    TXNID = models.CharField('TXN ID', max_length=100)
    ORDERID = models.CharField('ORDER ID',max_length=30)
    BANKTXNID = models.CharField('BANK TXN ID',max_length=100,)
    TXNAMOUNT = models.DecimalField('TXN AMOUNT',max_digits=50, decimal_places=2)
    CURRENCY = models.CharField('CURRENCY', max_length=4)
    TXNDATE = models.DateTimeField('TXN DATE',default=timezone.now)
    GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=30)
    BANKNAME = models.CharField('BANK NAME', max_length=50)
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10)
    RESPCODE = models.IntegerField('RESP CODE')
    RESPMSG = models.TextField('RESP MSG', max_length=250)
    STATUS = models.CharField('STATUS',max_length=12)
    CHECKSUMHASH = models.CharField(max_length=300)

    class Meta:
        db_table="Payment_Details"
    
    def __str__(self):
        return self.ORDERID + ' - ' + str(self.TXNAMOUNT)

    def __unicode__(self):
        return self.STATUS
