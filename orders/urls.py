from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # path('product/<int:product_id>/', product_detail_view, name='product_detail'),
    path('cart_adding/', views.cart_adding, name='cart_adding'),
]