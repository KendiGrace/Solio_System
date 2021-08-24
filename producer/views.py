
from django.shortcuts import render
from .admin import Producer
from.forms import ProducerRegistrationForm


def register_producer(request):
    if request.method == "POST":
        form = ProducerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = ProducerRegistrationForm
    return render(request, "register_producer.html", {"form": form})


def producer_list(request):
    producers = Producer.objects.all()
    return render(request, "producers_list.html", {"producers": producers})
# Create your views here.
