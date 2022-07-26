from mixer.backend.django import mixer
from decimal import Decimal
import pytest
from backend.apps.inventory.serializers import InventorySerializer, ItemDefinitionSerializer, ItemInstanceSerializer


@pytest.mark.django_db
class TestInventorySerializer:
    def test_serialize(self):
        item = mixer.blend('inventory.Inventory')
        ser = InventorySerializer(item)
        print(ser.data)
        keys_to_check = ['id','hidden']
        for key in keys_to_check:
            assert key in InventorySerializer.Meta.fields
            assert getattr(item, key) == ser.data.get(key)

        assert item.owner.id == ser.data.get('owner')
        assert item.party.id == ser.data.get('party')
        assert item.maximum_weight == Decimal(ser.data.get('maximum_weight'))


@pytest.mark.django_db
class TestItemInstanceSerializer:
    def test_serialize(self):
        item = mixer.blend('inventory.ItemInstance')
        ser = ItemInstanceSerializer(item)
        print(ser.data)
        keys_to_check = ['id','quantity','notes']
        for key in keys_to_check:
            assert key in ItemInstanceSerializer.Meta.fields
            assert getattr(item, key) == ser.data.get(key)

        assert item.definition.id == ser.data.get('definition')
        assert item.inventory.id == ser.data.get('inventory')


@pytest.mark.django_db
class TestItemDefinitionSerializer:
    def test_serialize(self):
        item = mixer.blend('inventory.ItemDefinition')
        ser = ItemDefinitionSerializer(item)
        print(ser.data)
        keys_to_check = ['id','name','description','fungible']
        for key in keys_to_check:
            assert key in ItemDefinitionSerializer.Meta.fields
            assert getattr(item, key) == ser.data.get(key)

        assert item.weight == Decimal(ser.data.get('weight'))
        assert item.value == Decimal(ser.data.get('value'))
