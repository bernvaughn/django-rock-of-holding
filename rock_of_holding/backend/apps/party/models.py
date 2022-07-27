from django.db import models
from django.utils.translation import gettext_lazy as _


class Party(models.Model):
    name = models.CharField(max_length=128, null=False)
    members = models.ManyToManyField('accounts.User', related_name='parties', through='Membership')

    @property
    def owner(self):
        mem = self.memberships.filter(role=Membership.Roles.OWNER).first()
        if mem is None:
            return None
        own = mem.user
        return own

    @property
    def owner_id(self):
        if self.owner is not None:
            return self.owner.id
        return None


class Membership(models.Model):

    class Roles(models.TextChoices):
        OWNER = 'OW', _('Owner')
        GAMEMASTER = 'GM', _('Game Master')
        PLAYER = 'PL', _('Player')

    user = models.ForeignKey('accounts.User', related_name='memberships', on_delete=models.CASCADE)
    party = models.ForeignKey('party.Party', related_name='memberships', on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=Roles.choices, default=Roles.PLAYER)
