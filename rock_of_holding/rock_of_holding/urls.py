from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('api/inventory/', include('backend.apps.inventory.urls')),
    path('api/party/', include('backend.apps.party.urls')),
]
