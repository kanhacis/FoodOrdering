from django.contrib import admin
from .models import Bag, BagItem

# Register Bag
@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
    list_display = ["user"]

admin.site.register(BagItem)