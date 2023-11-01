from django.db import models
from user.models import CustomUser
from menu.models import Menu

# Bag Model
class Bag(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class BagItem(models.Model):
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
