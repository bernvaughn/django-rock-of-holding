from django.shortcuts import render
from rest_framework import generics, status
from .models import Inventory, ItemDefinition, ItemInstance
from .serializers import InventorySerializer, ItemDefinitionSerializer, ItemInstanceSerializer


# TODO: test for this
class InventoryView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


# TODO: test for this
class ItemDefinitionView(generics.ListAPIView):
    queryset = ItemDefinition.objects.all()
    serializer_class = ItemDefinitionSerializer


# TODO: test for this
class ItemInstanceView(generics.ListAPIView):
    queryset = ItemInstance.objects.all()
    serializer_class = ItemInstanceSerializer
