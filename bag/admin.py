from django.contrib import admin
from .models import Bag, BagItem

# Register Bag
admin.site.register(Bag)
admin.site.register(BagItem)