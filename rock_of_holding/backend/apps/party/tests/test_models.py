from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestParty:
    def test_create(self):
        item = mixer.blend('party.Party')
        assert item is not None


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
