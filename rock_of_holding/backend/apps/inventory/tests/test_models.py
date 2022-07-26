from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestInventory:
    def test_create(self):
        item = mixer.blend('inventory.Inventory')
        assert item is not None

    def test_current_weight(self):
        inv = mixer.blend('inventory.Inventory', maximum_weight=2)
        item_def = mixer.blend('inventory.ItemDefinition', weight=2)
        item_inst = mixer.blend('inventory.ItemInstance', quantity=1, definition=item_def, inventory=inv)

        assert inv.items.count() == 1
        assert item_inst.weight == 2
        assert inv.current_weight == 2

    def test_current_weight_multiple(self):
        inv = mixer.blend('inventory.Inventory', maximum_weight=2)
        item_def = mixer.blend('inventory.ItemDefinition', weight=2)
        item_inst1 = mixer.blend('inventory.ItemInstance', quantity=1, definition=item_def, inventory=inv)
        item_inst2 = mixer.blend('inventory.ItemInstance', quantity=2, definition=item_def, inventory=inv)
        item_inst3 = mixer.blend('inventory.ItemInstance', quantity=3, definition=item_def, inventory=inv)

        assert item_inst1.weight == 2
        assert item_inst2.weight == 4
        assert item_inst3.weight == 6
        assert inv.current_weight == 6 + 4 + 2

    def test_maximum_weight(self):
        inv = mixer.blend('inventory.Inventory', maximum_weight=2)
        item_def = mixer.blend('inventory.ItemDefinition', weight=2)
        item_inst = mixer.blend('inventory.ItemInstance', quantity=1, definition=item_def, inventory=inv)

        assert inv.current_weight == 2
        assert inv.maximum_weight == 2
        assert inv.over_weight is False

        item_def.weight = 3
        item_def.save()

        assert inv.current_weight == 3
        assert inv.maximum_weight == 2
        assert inv.over_weight is True


@pytest.mark.django_db
class TestItemInstance:
    def test_create(self):
        item = mixer.blend('inventory.ItemInstance')
        assert item is not None

    def test_weight(self):
        item = mixer.blend('inventory.ItemInstance', quantity=1)

        assert item.weight == item.definition.weight

        item.quantity = 2
        item.save()

        assert item.weight == 2 * item.definition.weight


@pytest.mark.django_db
class TestItemDefinition:
    def test_create(self):
        item = mixer.blend('inventory.ItemDefinition')
        assert item is not None
