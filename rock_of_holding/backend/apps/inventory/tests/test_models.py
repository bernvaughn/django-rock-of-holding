from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestInventory:
    def test_create(self):
        item = mixer.blend('inventory.Inventory')
        assert item is not None


@pytest.mark.django_db
class TestItemInstance:
    def test_create(self):
        item = mixer.blend('inventory.ItemInstance')
        assert item is not None


@pytest.mark.django_db
class TestItemDefinition:
    def test_create(self):
        item = mixer.blend('inventory.ItemDefinition')
        assert item is not None
