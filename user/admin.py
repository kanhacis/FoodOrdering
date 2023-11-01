from django.contrib import admin
from .models import CustomUser, Address

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "mobile", "user_type"]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["state", "city", "area", "zipcode", "category"]