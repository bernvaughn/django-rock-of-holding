from django.db import models


class Inventory(models.Model):
    owner = models.ForeignKey('accounts.User', related_name='inventories', on_delete=models.CASCADE)
    party = models.ForeignKey('party.Party', related_name='inventories', on_delete=models.CASCADE)
    maximum_weight = models.IntegerField()


class ItemInstance(models.Model):
    definition = models.ForeignKey('inventory.ItemDefinition', related_name='instances', null=False, on_delete=models.CASCADE)
    inventory = models.ForeignKey('inventory.Inventory', related_name='items', null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)
    notes = models.TextField(max_length=3000)


class ItemDefinition(models.Model):
    name = models.CharField(max_length=128, null=False)
    description = models.TextField(max_length=3000)
    weight = models.IntegerField()
    value = models.IntegerField()
    fungible = models.BooleanField(null=False, default=False)
