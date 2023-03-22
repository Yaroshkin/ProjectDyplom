from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('catalogs',views.catalogs),
    path('about',views.about),
    path('telephone',views.phone),
    path('notebook',views.notebook),
    path('accesory',views.accesory),
    path('register',views.register)
]