from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class PollView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class GetRoomView(APIView):
    serializer_class = PollSerializer
    lookup_url_kwarg = 'code'

    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            poll = Poll.objects.filter(code=code).first()
            if poll is not None:
                data = PollSerializer(poll[0]).data
                data['is_host'] = self.request.session.session_key == poll[0].host
                return Response(data,status=status.HTTP_200_OK)
            return Response({'Room not found': 'Invalid Room Code'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'Code paramater not found in request.'},status=status.HTTP_400_BAD_REQUEST)


class JoinPollView(APIView):
    lookup_url_kwarg='code'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        code = request.data.get(self.lookup_url_kwarg)
        if code != None:
            poll = Poll.objects.filter(code=code).first()
            if poll is not None:
                self.request.session['room_code'] = code
                return Response({'message': 'Room joined!'}, status=status.HTTP_200_OK)
            return Response({'Bad Request': 'Invalid room code'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'Bad Request': 'Invalid post data, did not find a matching room'}, status=status.HTTP_400_BAD_REQUEST)

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

            self.request.session['room_code'] = poll.code
            return Response(PollSerializer(poll).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class UserInRoom(APIView):
    def get(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        data = {
            'code': self.request.session.get('room_code')
        }

        return JsonResponse(data, status=status.HTTP_200_OK)
