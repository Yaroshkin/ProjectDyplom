from django.shortcuts import render
from main.models import *
def catalog(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_telephone = products_images.filter(product__category_id=1)
    products_images_notebook = products_images.filter(product__category_id=2)
    products_images_acsessory = products_images.filter(product__category_id=3)
    return render(request, 'catalog.html', locals())



def home(request):
    return render(request,'home.html')

def cart(request):
    return render(request,'cart.html')

def about(request):
    return render(request,'about.html')