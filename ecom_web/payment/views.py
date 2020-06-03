from django.shortcuts import render,redirect,get_object_or_404
from payment.models import Order,pay
from cart.models import Cart
import json
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
from PayTm import Checksum
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




MERCHANT_KEY = 'fspy#kzkpCIc@oO@'
# Create your views here.

@ensure_csrf_cookie
def checkout_page(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    user = request.user
    status = False
    if pay.objects.filter(user=user, STATUS = 'TXN_SUCCESS'):
        trns = pay.objects.filter(user=user, STATUS = 'TXN_SUCCESS')[0]
        status = True
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name', '')
            phone = request.POST.get('phone', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')
            amount = cart_obj.total
            order = Order(name=name,phone=phone,email=email,address=address,city=city,state=state,zip_code=zip_code)
            order.save()
            # Request paytm to transfer the amount to your account after payment by user
            param_dict = {

                    'MID': 'QNsvNs85056236851568',
                    'ORDER_ID': str(order.order_id),
                    'TXN_AMOUNT': str(amount),
                    'CUST_ID': email,
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': 'WEBSTAGING',
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'paytm.html', {'param_dict': param_dict,'user': user})
        return render(request,'checkout.html',{'cart' : cart_obj,'status': status})
    else:
        return redirect('user:user_login')

@csrf_exempt
def recipt(request):
    form = request.POST
    user=request.user
    param_dict = {}
    for i in form.keys():
        param_dict[i] = form[i]
    pay.objects.create(user=request.user, **param_dict)

    status = 'TXN_FAILURE'
    for key,value in param_dict.items():
        if key == 'STATUS':
            # user.user_details.status = value
            # user.user_details.save()
            # if value == 'TXN_SUCCESS':
            status = value
    return render(request, "receipt.html", {"paytmr": param_dict,"status": status})

@csrf_exempt
def handlerequest(request):       
    #paytm will send post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    response_dict['CHECKSUMHASH'] = checksum
    # p = pay()
    # p.merchant_id = response_dict['MID']
    # p.transaction_id = response_dict['TXNID']
    # p.order_id = response_dict['ORDERID']
    # p.bank_txn_id = response_dict['BANKTXNID']
    # p.txn_amount = response_dict['TXNAMOUNT']
    # p.currency = response_dict['CURRENCY']
    # p.txn_date = response_dict['TXNDATE']
    # p.gateway_name = response_dict['GATEWAYNAME']
    # p.bank_name = response_dict['BANKNAME']
    # p.payment_mode = response_dict['PAYMENTMODE']
    # p.payment_status = response_dict['STATUS']
    # p.checksumhash = response_dict['CHECKSUMHASH']
    # p.save()
    return render(request, 'paymentstatus.html', {'response': response_dict})
