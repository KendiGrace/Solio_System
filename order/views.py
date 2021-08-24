
from django.shortcuts import render
from .admin import Order
from.forms import OrderRegistrationForm


def register_orders(request):
    if request.method == "POST":
        form = OrderRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = OrderRegistrationForm
    return render(request, "register_orders.html", {"form": form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, "order_list.html", {"order": orders})
# Create your views here.



# Create your views here.
