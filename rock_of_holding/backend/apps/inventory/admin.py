from django.contrib import admin
from .models import Inventory, ItemDefinition, ItemInstance

admin.register(Inventory)
admin.register(ItemDefinition)
admin.register(ItemInstance)
