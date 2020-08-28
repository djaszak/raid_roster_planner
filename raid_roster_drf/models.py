from raid_roster_drf import constants

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)


class GameClass(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=constants.ROLES)
    color = models.CharField(max_length=255, choices=constants.CLASS_COLOURS)
    icon = models.FileField()


class Character(models.Model):
    name = models.CharField(max_length=255)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_class = models.ManyToManyField(GameClass)
    armory_link = models.URLField(blank=True)
