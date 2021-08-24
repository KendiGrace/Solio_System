from django.db import models
class Product(models.Model):
    product_name=models.CharField(max_length=18)
    product_id=models.CharField(max_length=20)
    product_image=models.ImageField()
    product_supplier=models.CharField(max_length=18)
    product_price=models.CharField(max_length=10)
    category=(
        (u'F',u'Fruits'),
        (u'G',u'Groceries'),
        (u'M',u'Meat'),
        (u'S',u'Spices')
    )
    product_category=models.CharField(max_length=1,choices=category)

def __str__(self):
    return self.product_name

# Create your models here.
