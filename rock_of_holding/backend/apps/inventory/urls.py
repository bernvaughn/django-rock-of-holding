from django.urls import path
from .views import InventoryView, ItemDefinitionView, ItemInstanceView


# TODO: tests for these
urlpatterns = [
    path('inventory', InventoryView.as_view()),
    path('itemdefinition', ItemDefinitionView.as_view()),
    path('iteminstance',ItemInstanceView.as_view()),
]
