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
    player_name = forms.CharField(label=_('Your Nickname'))

    # character model
    character_name = forms.CharField(label=_('Character Name'))
    game_class = forms.ModelChoiceField(label=_('Class'), queryset=models.GameClass.objects.all())
    main_role = forms.ModelChoiceField(label=_('Main Role'), queryset=models.Role.objects.all())
    off_spec_roles = forms.ModelMultipleChoiceField(label=_('Off-Spec Roles'), queryset=models.Role.objects.all())
    is_main = forms.BooleanField(label=_('This character is your Main.'), required=False)

    def clean(self):
        game_class = self.cleaned_data['game_class']
        main_role = self.cleaned_data['main_role']
        off_spec_roles = self.cleaned_data['off_spec_roles']

        possible_roles = constants.CLASS_ROLE_MAPPING[game_class.name]
        possible_roles_human_readable = ', '.join(possible_roles)

        roles_valid = True

        if main_role not in possible_roles:
            roles_valid = False

        for rl in off_spec_roles:
            if rl.name not in possible_roles:
                roles_valid = False

        if not roles_valid:
            raise forms.ValidationError(_(f'The class you chose cannot fulfill one of the roles you chose. '
                                          f'Possible roles for this class are: {possible_roles_human_readable}'))
