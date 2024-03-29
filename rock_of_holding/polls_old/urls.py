from django.urls import path
from .views import *

urlpatterns = [
    path('', PollView.as_view()),
    path('createpoll', CreatePollView.as_view()),
    path('getroom',GetRoomView.as_view()),
    path('joinroom',JoinPollView.as_view()),
    path('userinroom',UserInRoom.as_view()),
    path('leaveroom',LeaveRoom.as_view()),
    path('updateroom',UpdateRoom.as_view()),
]