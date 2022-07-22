from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class PollView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class CreatePollView(APIView):
    serializer_class = CreatePollSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            host = self.request.session.session_key

            queryset = Poll.objects.filter(host=host)
            if queryset.exists():
                poll = queryset.first()
                poll.title = title
                poll.save(update_fields=['title'])
            else:
                poll = Poll()
                poll.host = host
                poll.title = title
                poll.save()

            return Response(PollSerializer(poll).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)