from django.shortcuts import render
from rest_framework import generics, status
from .models import Party, Membership
from .serializers import PartySerializer, MembershipSerializer


# TODO: test for this
class PartyView(generics.ListAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


# TODO: test for this
class MembershipView(generics.ListAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
