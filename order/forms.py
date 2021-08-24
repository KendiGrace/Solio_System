from django import forms
from django.db.models.base import Model
from .models import Order

class OrderRegistrationForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"