
from django.db import models

from raid_roster_planner.raid_roster_drf import constants


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
        capitalized_list = [x.capitalize() for x in self.name.split('_')]
        return ' '.join(capitalized_list)


class Character(models.Model):
    name = models.CharField(max_length=255)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_class = models.ForeignKey(GameClass, on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    armory_link = models.URLField(blank=True)
    is_main = models.BooleanField()

    def __str__(self):
        return self.name

    @property
    def role_string(self):
        role_string_list = [str(role) for role in self.role.all()]
        return ', '.join(role_string_list)
    
    @property
    def get_colour(self):
        return constants.CLASS_COLOURS[self.game_class.name]
