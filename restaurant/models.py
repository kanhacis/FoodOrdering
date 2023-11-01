from django.db import models
from user.models import CustomUser, Address


CUISINE_CHOICES = (
        ('indian', 'Indian'),
        ('italian', 'Italian'),
        ('chinese', 'Chinese'),
        ('japanese', 'Japanese'),
        ('american', 'American')
    )

VEG_CHOICES = (
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
        ('both', 'Both'),
    )
# Restaurant Model
class Restaurant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="restaurants", 
                                limit_choices_to={'user_type': 'foodprovider'})
    name = models.CharField(max_length=150) 
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    # branch = 
    is_verified = models.BooleanField(default=False) 
    cuisine = models.CharField(max_length=100, choices=CUISINE_CHOICES) 
    veg_or_nonveg = models.CharField(max_length=50, choices=VEG_CHOICES)

    def __str__(self):
        return self.name


# Review Model (For restaurants)
class Review(models.Model):
    rating = models.PositiveIntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")
    description = models.TextField(blank=True)
    date = models.DateField()