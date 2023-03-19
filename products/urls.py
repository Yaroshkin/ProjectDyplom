from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('product/<int:product_id>/', product, name='product'),

]