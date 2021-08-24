
from django.urls import path
from django import urls
from django.urls.resolvers import URLPattern
from .views import register_products, products_list

urlpatterns = [
    path("register/", register_products, name="register_products"),
    path("list/", products_list, name="products_list")]