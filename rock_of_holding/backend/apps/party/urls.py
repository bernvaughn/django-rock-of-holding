from django.urls import path
from .views import MembershipView, PartyView


# TODO: tests for these
urlpatterns = [
    path('party', PartyView.as_view()),
    path('membership', MembershipView.as_view()),
]
