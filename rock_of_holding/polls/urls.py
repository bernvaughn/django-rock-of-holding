from django.urls import path
from .views import *

urlpatterns = [
    path('', PollView.as_view()),
]