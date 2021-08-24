from django.urls import path
from .views import register_customer,customer_list
urlpatterns=[
    path("register/",register_customer,name="register_customer"),
    path("list/", customer_list,name = "customer_list"),
]