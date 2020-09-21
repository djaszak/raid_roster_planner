
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
    main_role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='main_spec_characters')
    off_spec_roles = models.ManyToManyField(Role, related_name='off_spec_characters', blank=True)
    armory_link = models.URLField(blank=True)
    is_main = models.BooleanField()

    def __str__(self):
        return self.name

    @property
    def off_spec_role_string(self):
        role_string_list = [str(role) for role in self.off_spec_roles.all()]
        return ', '.join(role_string_list)

    @property
    def get_colour(self):
        return constants.CLASS_COLOURS[self.game_class.name]

    @property
    def get_class_name(self):
        return f'{self.game_class}' + ' *' if self.off_spec_roles.exists() else ''

    @property
    def get_armory_link(self):
        return f'https://worldofwarcraft.com/en-gb/character/{constants.SERVER_REGION}/{constants.SERVER_NAME}/{self.name.lower()}' if not self.armory_link \
            else self.armory_link
