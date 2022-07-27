from rest_framework import serializers
from .models import Inventory, ItemInstance, ItemDefinition


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'name',
            'owner',
            'party',
            'maximum_weight',
            'hidden',
            'current_weight',
            'over_weight',
        ]


class ItemInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInstance
        fields = [
            'id',
            'definition',
            'inventory',
            'quantity',
            'notes',
            'weight',
        ]


class ItemDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDefinition
        fields = [
            'id',
            'name',
            'description',
            'weight',
            'value',
            'fungible',
        ]
