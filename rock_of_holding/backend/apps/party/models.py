from django.db import models
from django.utils.translation import gettext_lazy as _


class Party(models.Model):
    name = models.CharField(max_length=128, null=False)
    members = models.ManyToManyField('accounts.User', related_name='parties', through='Membership')


class Membership(models.Model):

    class Roles(models.TextChoices):
        OWNER = 'OW', _('Owner')
        GAMEMASTER = 'GM', _('Game Master')
        PLAYER = 'PL', _('Player')

    user = models.ForeignKey('accounts.User', related_name='party_memberships', on_delete=models.CASCADE)
    party = models.ForeignKey('party.Party', related_name='user_memberships', on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=Roles.choices, default=Roles.PLAYER)
