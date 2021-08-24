from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    date_of_birth = models.DateTimeField
    phone_number = models.CharField(max_length=13)
    id_number = models.CharField(max_length=12)
    email = models.EmailField()
    Image = models.ImageField()
    Location = models.CharField(max_length=16)
    gender = (
        (u'F', u'Female'),
        (u'M', u'Male'),
        (u'O', u'Others')
    )
    gender = models.CharField(max_length=1, choices=gender)
    profession = models.CharField(max_length=16)
    income = models.PositiveBigIntegerField()

    def __str__(self):
        return self.first_name
 

# Create your models here.
