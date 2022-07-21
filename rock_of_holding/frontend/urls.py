from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('join', index),
    path('join/<roomcode>', index),
    path('create', index)
]