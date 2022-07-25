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
                data = PollSerializer(poll).data
                print(self.request.session.session_key, poll.host) # TODO: remove
                print(self.request.session.session_key == poll.host)
                data['is_host'] = self.request.session.session_key == poll.host
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


class LeaveRoom(APIView):
    def post(self, request, fromat=None): # should probably have been patch
        if 'room_code' in self.request.session:
            code = self.request.session.pop('room_code')

            host_id = self.request.session.session_key
            room = Poll.objects.filter(host=host_id).first()
            if room is not None:
                room.delete()

        return Response({'Message': 'Success'}, status=status.HTTP_200_OK)


class UpdateRoom(APIView):
    serializer_class = UpdatePollSerializer

    def patch(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            code = serializer.data.get('code')
            title = serializer.data.get('title')

            room = Poll.objects.filter(code=code).first()
            if room is None:
                return Response({'msg': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)

            user_id = self.request.session.session_key()
            if room.host != user_id:
                return Response({'msg': 'you are not the host'}, status=status.HTTP_403_FORBIDDEN)

            room.title = title
            room.save(update_fields=['title'])
            return Response(PollSerializer(room).data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
