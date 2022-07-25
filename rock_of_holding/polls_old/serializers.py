from rest_framework import serializers
from .models import *

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id','code','host','title')


class CreatePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('title',)


class UpdatePollSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[]) 
    # redifine code so we ignore its unique contraint?

    class Meta:
        model = Poll
        fields = ('title', 'code')
