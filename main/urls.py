from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('catalog',views.catalog),
    path('cart', views.cart),
    path('about',views.about),
    path('catalog/telephone',views.phone),
    path('catalog/notebook',views.notebook)
]