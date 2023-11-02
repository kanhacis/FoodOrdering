from django.contrib import admin
from .models import Restaurant, Review

# Register Restaurant
admin.site.register(Restaurant)

# Register Review
admin.site.register(Review)