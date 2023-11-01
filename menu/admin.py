from django.contrib import admin
from .models import Menu

# Register Menu Model
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["restaurant", "name", "description", "type", "price", "image1"]