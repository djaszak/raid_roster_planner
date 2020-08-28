
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)


class Role(models.Model):
    name = models.CharField(max_length=255)


class GameClass(models.Model):
    name = models.CharField(max_length=255)


class Character(models.Model):
    name = models.CharField(max_length=255)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_class = models.ForeignKey(GameClass, on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    armory_link = models.URLField(blank=True)