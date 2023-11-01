from django.contrib import admin
from .models import Order, OrderItem

# Register Order Model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "restaurant", "estimated_time", "is_confirmed", "status"]

admin.site.register(OrderItem)