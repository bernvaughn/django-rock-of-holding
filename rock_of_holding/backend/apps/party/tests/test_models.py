from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestParty:
    def test_create(self):
        item = mixer.blend('party.Party')
        assert item is not None

    def test_owner(self):
        user = mixer.blend('accounts.User')
        party = mixer.blend('party.Party')
        mem = mixer.blend('party.Membership',user=user,party=party,role='OW')

        assert party.owner == user

    def test_owner_id(self):
        user = mixer.blend('accounts.User')
        party = mixer.blend('party.Party')
        mem = mixer.blend('party.Membership',user=user,party=party,role='OW')

        assert party.owner == user
        assert party.owner_id == user.id

    def test_owner_none(self):
        party = mixer.blend('party.Party')

        assert party.owner is None


@pytest.mark.django_db
class TestMembership:
    def test_create(self):
        item = mixer.blend('party.Membership')
        assert item is not None

    def test_roles(self):
        item = mixer.blend('party.Membership')
        print(item.Roles.values)
        assert 'OW' in item.Roles.values
        assert 'GM' in item.Roles.values
        assert 'PL' in item.Roles.values
