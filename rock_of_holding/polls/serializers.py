from rest_framework import serializers
from .models import *

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id','code','host')
