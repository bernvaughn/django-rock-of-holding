from rest_framework import serializers
from .models import Inventory, ItemInstance, ItemDefinition


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'owner',
            'party',
            'maximum_weight',
            'hidden',
            # TODO: add over_weight bool? 
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
