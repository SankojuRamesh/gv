from django.shortcuts import render
from .models import OrderModel as Order
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import razorpay 
from .constants import PaymentStatus 
from accountmanager.models import ShippmentModel
from ordermanager.models import CartModel,OrderProductsModel
import json

def order_payment(request):
    if request.method == "POST":
        name =''  # request.POST.get("name")
        amount = request.POST.get("amount")
        orderquentity = request.POST.get("orderquentity")
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))



        
        shipping = ShippmentModel.objects.filter(user=request.user).filter(status=1).first()
        razorpay_order = client.order.create(
            {"amount": int(float(amount)) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Order.objects.create(orderprice=amount, 
            name=name, amount=amount, provider_order_id=razorpay_order["id"], orderby_id=request.user.id,shippingid=shipping.id
        )
        order.save()
        for orderdetails in CartModel.objects.filter(user=request.user):
            OrderProductsModel.objects.create(orderid=order,productid=orderdetails.productid, productQuntity= orderdetails.quantity)
        CartModel.objects.filter(user=request.user).delete()
        return render(
            request,
            "frontend/payment.html",
            {
                "callback_url": "http://" + "localhost:8000" + "/callback/",
                "razorpay_key": settings.RAZORPAY_API_KEY,
                "order": order,
            },
        )
    return render(request, "frontend/payment.html")


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        return client.utility.verify_payment_signature(response_data)  
    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.paymentid=payment_id
        order.signature_id = signature_id
        order.save()
        
        if  verify_signature(request.POST):            
            order.status = PaymentStatus.SUCCESS       
             
            order.save()
            
            return render(request, "frontend/sucess.html", context={"status": order})
        else:
            order.status = PaymentStatus.FAILURE
            # order.payment_method = data.get("method", "Unknown")
             
            order.save()
             
            return render(request, "frontend/callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        print("---------------------333")
        return render(request, "frontend/faluer.html", context={"status": order.status})