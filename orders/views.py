from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .forms import CheckoutContactForm
from django.contrib.auth.models import User

# Create your views here.
def cart_adding(request):
    return_dict= dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("id_prod")
    nmb = data.get("number")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInCart.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInCart.objects.get_or_create(session_key=session_key,product_id=product_id,is_active=True,defaults={"nmb":nmb})
        if not created:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_cart.count()
    return_dict["prod_total"] = products_total_nmb

    return_dict["prod"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["prod"].append(product_dict)

    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    product_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            name = data.get("name",None)
            phone = data["phone"]
            user, created = User.objects.get_or_create(username=phone,defaults={"first_name": name})

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)

            for name, value in data.items():
                if name.startswith("product_cart_"):
                    prod_in_cart_id = name.split("product_cart_")[1]
                    prod = ProductInCart.objects.get(id=prod_in_cart_id)
                    prod.nmb = value
                    prod.save(force_update=True)
                    ProductInOrder.objects.create(product=prod.product, nmb=prod.nmb,price_per_item=prod.price_per_item, total_price=prod.total_price,order=order)
        else:
            print("no")
    return render(request,'order/checkout.html',locals())
