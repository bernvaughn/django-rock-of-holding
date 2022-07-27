from django.db import models
from django.core.validators import MinValueValidator


class Inventory(models.Model):
    name = models.CharField(max_length=128, null=False)
    owner = models.ForeignKey('accounts.User', related_name='inventories', on_delete=models.CASCADE)
    party = models.ForeignKey('party.Party', related_name='inventories', on_delete=models.CASCADE)
    maximum_weight = models.DecimalField(max_digits=12, decimal_places=3, validators=[MinValueValidator(0.0)])
    hidden = models.BooleanField(null=False, default=False)

    @property
    def current_weight(self):
        weight = 0
        for item in self.items.all():
            weight += item.weight
        return weight

    @property
    def over_weight(self):
        if self.current_weight > self.maximum_weight:
            return True
        return False


class ItemInstance(models.Model):
    # defines an item that is in an inventory
    # like a line item on a bom
    definition = models.ForeignKey('inventory.ItemDefinition', related_name='instances', null=False, on_delete=models.CASCADE)
    inventory = models.ForeignKey('inventory.Inventory', related_name='items', null=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, default=1)
    notes = models.TextField(max_length=3000)

    @property
    def weight(self):
        return self.definition.weight * self.quantity


class ItemDefinition(models.Model):
    # defines an item
    name = models.CharField(max_length=128, null=False)
    description = models.TextField(max_length=3000)
    weight = models.DecimalField(max_digits=12, decimal_places=3, validators=[MinValueValidator(0.0)])
    value = models.DecimalField(max_digits=12, decimal_places=3, validators=[MinValueValidator(0.0)])
    fungible = models.BooleanField(null=False, default=False)
