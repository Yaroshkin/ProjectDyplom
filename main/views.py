from django.shortcuts import render
from main.models import *
def catalog(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'catalog.html', locals())

def home(request):
    return render(request,'home.html')

def cart(request):
    return render(request,'cart.html')

def about(request):
    return render(request,'about.html')