from django import forms
from django.utils.translation import ugettext as _

from raid_roster_planner.raid_roster_drf import models, constants


class PlayerForm(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = '__all__'


class CharacterForm(forms.ModelForm):
    class Meta:
        model = models.Character
        fields = '__all__'


class InputForm(forms.Form):
    # player model
    player_name = forms.CharField(label=_('Your Player Name'))

    # character model
    character_name = forms.CharField(label=_('Character Name'))
    game_class = forms.ChoiceField(label=_('Class'), choices=constants.CLASS_FORM_CHOICES)
    role = forms.ModelMultipleChoiceField(label=_('Role'), queryset=models.Role.objects.all())
    is_main = forms.BooleanField(label=_('This character is your Main.'))

