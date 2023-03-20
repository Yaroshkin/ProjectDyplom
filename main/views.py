from django.shortcuts import render
from products.models import *
def catalogs(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_telephone = products_images.filter(product__category_id=1)
    products_images_notebook = products_images.filter(product__category_id=2)
    products_images_acsessory = products_images.filter(product__category_id=3)
    return render(request, 'product/catalog.html', locals())

def phone(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_telephone = products_images.filter(product__category_id=1)
    return render(request, 'product/phone.html', locals())

def notebook(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_notebook = products_images.filter(product__category_id=2)
    return render(request, 'product/notebook.html', locals())

def accesory(request):
    products_images = ProductImage.objects.filter(is_active=True,is_main=True)
    products_images_accesory = products_images.filter(product__category_id=3)
    return render(request, 'product/accsesory.html', locals())

def home(request):
    return render(request,'home.html')

def cart(request):
    return render(request,'')

def about(request):
    return render(request,'about.html')