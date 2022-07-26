from mixer.backend.django import mixer
import pytest
from backend.apps.party.serializers import PartySerializer, MembershipSerializer


@pytest.mark.django_db
class TestPartySerializer:
    def test_serialize(self):
        item = mixer.blend('party.Party')
        ser = PartySerializer(item)
        print(ser.data)
        keys_to_check = ['id','name', 'owner']
        for key in keys_to_check:
            assert key in PartySerializer.Meta.fields
            assert getattr(item, key) == ser.data.get(key)

    def test_serialize_members(self):
        party = mixer.blend('party.Party')
        u1 = mixer.blend('accounts.User')
        u2 = mixer.blend('accounts.User')
        m1 = mixer.blend('party.Membership', user=u1, party=party)
        m2 = mixer.blend('party.Membership', user=u2, party=party)
        ser = PartySerializer(party)
        print(ser.data)
        
        assert len(ser.data.get('members')) > 0
        assert u1.id in ser.data.get('members')
        assert u2.id in ser.data.get('members')


@pytest.mark.django_db
class TestMembershipSerializer:
    def test_serialize(self):
        item = mixer.blend('party.Membership')
        ser = MembershipSerializer(item)
        print(ser.data)
        keys_to_check = ['id','role']
        for key in keys_to_check:
            assert key in MembershipSerializer.Meta.fields
            assert getattr(item, key) == ser.data.get(key)

        assert item.user.id == ser.data.get('user')
        assert item.party.id == ser.data.get('party')
