from django.urls import path
from .views import producer_list, register_producer
urlpatterns=[
    path("register/",register_producer,name="register_producer"),
    path("list/", producer_list,name="producer_list"),
    ]