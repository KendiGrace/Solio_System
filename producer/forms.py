from django import forms
from django.db.models.base import Model
from .models import Producer


class ProducerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = "__all__"
