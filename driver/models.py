from django.db import models
from user.models import CustomUser

# Delivery Mode
class Delivery(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type':'delivery'})
    is_verified = models.BooleanField(default=False) 

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name