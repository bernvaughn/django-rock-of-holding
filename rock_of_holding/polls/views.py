from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class PollView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
