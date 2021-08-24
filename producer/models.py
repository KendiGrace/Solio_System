from django.db import models


class Producer(models.Model):
    image = models.FileField(null=True, blank=True)
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    id_number = models.CharField(max_length=12)
    farm_number = models.CharField(max_length=12)
    farm_title_deed = models.FileField()
    gender = (
        (u'F', u'Female'),
        (u'M', u'Male'),
        (u'O', u'Other'),

    )
    products = models.CharField(max_length=1, choices=gender)
    products = (
        (u'G', u'Groceries'),
        (u'F', u'Fruits'),
        (u'D', u'Dairies'),
        (u'M', u'Meat')
    )
    products = models.CharField(max_length=1, choices=products)
    region = (
        (u'N', u'Nairobi'),
        (u'K', u'Kiambu'),
        (u'KD', u'Narok'),
        (u'N', u'Nyeri'),
        (u'T', u'Thika'),
        (u'E', u'Embu'),
        (u'MR', u'Meru')

    )

    region = models.CharField(max_length=3, choices=region)

    def __str__(self):
        return self.first_name

# Create your models here.
