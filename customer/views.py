from customer.models import Customer
from django.shortcuts import render
from.forms import CustomerRegistrationForm


def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = CustomerRegistrationForm
    return render(request, "register_customer.html", {"form": form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customers_list.html", {"customers": customers})
# Create your views here.


# Create your views here.
