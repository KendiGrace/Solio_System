from product .models import Product
from django.shortcuts import render
from .forms import Product, ProductRegistrationForm 
# Create your views here.


def register_products(request):
    if request.method == "POST":
        form = ProductRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = ProductRegistrationForm()

    return render(request, "register_product.html", {"form": form})


def products_list(request):
  products = Product.objects.all()
  return render(request, "product_list.html", {"product": products})


# Create your views here.
