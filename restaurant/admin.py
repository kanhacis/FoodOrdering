from django.contrib import admin
from .models import Restaurant, Review

# Register Restaurant
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "address", "mobile", "is_verified", "cuisine", "veg_or_nonveg"]

# Register Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["rating", "user", "restaurant", "description", "date"]