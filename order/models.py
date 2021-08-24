from django.db import models
from django.db.models.fields import CharField

class Order(models.Model):
    order_id=models.CharField(max_length=20)
    order_client=models.CharField(max_length=20)
    order_location=models.CharField(max_length=20)
    order_date=models.DateTimeField()
    order_cost=models.CharField(max_length=15)

    def __str__(self):
        return self.order_client


# Create your models here.
