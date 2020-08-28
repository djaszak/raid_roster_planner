
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GameClass(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_class = models.ForeignKey(GameClass, on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    armory_link = models.URLField(blank=True)
    is_main = models.BooleanField()

    def __str__(self):
        return self.name
