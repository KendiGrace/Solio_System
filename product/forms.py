from django import forms
from django.db.models.base import Model
from .models import Product

class ProductRegistrationForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"