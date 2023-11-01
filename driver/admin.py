from django.contrib import admin
from .models import Delivery

# Register Delivery Model
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ["user", "is_verified"]