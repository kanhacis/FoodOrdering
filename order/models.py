from django.db import models
from user.models import CustomUser
from restaurant.models import Restaurant
from menu.models import Menu
from driver.models import Delivery


STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled') 
    )
# Order Model
class Order(models.Model):
    # order_id = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    estimated_time = models.TimeField()
    is_confirmed = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return  self.user.first_name #"#" + self.order_id + " @ " +


class OrderItem(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

   


