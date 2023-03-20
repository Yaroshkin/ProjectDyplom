from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('<int:product_id>', product, name='product'),

]