from django.contrib import admin
from .models import Inventory, ItemDefinition, ItemInstance

admin.site.register(Inventory)
admin.site.register(ItemDefinition)
admin.site.register(ItemInstance)
