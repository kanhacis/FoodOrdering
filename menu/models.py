from django.db import models
from restaurant.models import Restaurant, Review


TYPE_CHOICES = (
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
    )
# Menu Model
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

    price = models.PositiveIntegerField()
    # rating = models.ForeignKey(Review, on_delete=models.CASCADE, blank=True)
    image1 = models.ImageField(upload_to="menu_images/")
    image2 = models.ImageField(upload_to="menu_images/", blank=True)
    image3 = models.ImageField(upload_to="menu_images/", blank=True)
