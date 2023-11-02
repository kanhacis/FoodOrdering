from django.contrib.auth.models import AbstractUser
from django.db import models


USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('foodprovider', 'Food Provider'),
        ('delivery', 'Delivery Management'),
    )
# Custom User Model
class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15)
    user_type = models.CharField(max_length=25, choices=USER_TYPE_CHOICES)


CATEGORY_CHOICES = (
        ('home', 'Home'),
        ('work', 'Work'),
        ('class', 'Class'),
    )
# Address Model
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    landmark = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
