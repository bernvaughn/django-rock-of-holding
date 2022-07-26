from rest_framework import serializers
from .models import Party, Membership


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = [
            'id',
            'name',
            'members',
            'owner',
        ]


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = [
            'id',
            'user',
            'party',
            'role',
        ]
