from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('home', views.index, name="index"),
    path('shop', views.shop, name="shop"),
    path('contact', views.contact, name="contact"),
    path('apply', views.apply, name="apply"),
]