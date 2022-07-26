from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestUser:
    def test_create(self):
        item = mixer.blend('accounts.User')
        assert item is not None
