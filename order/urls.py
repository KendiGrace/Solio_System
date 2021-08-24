
from django.urls import path
from django import urls
from django.urls.resolvers import URLPattern
from .views import register_orders, order_list

urlpatterns = [
    path("register/", register_orders, name="register_orders"),
    path("list/", order_list, name="order_list")]
