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
    off_spec_roles = forms.ModelMultipleChoiceField(label=_('Off-Spec Roles'),
                                                    queryset=models.Role.objects.all(),
                                                    required=False)
    is_main = forms.BooleanField(label=_('This character is your Main.'), required=False)

    def clean_is_main(self):
        data = self.cleaned_data['is_main']

        if data:
            if models.Character.objects.filter(is_main=data, player__name=self.data['player_name']).exists:
                raise forms.ValidationError(_('As a player you can only have one main character.'))

        return data

    def clean_character_name(self):
        data = self.cleaned_data['character_name']

        if models.Character.objects.filter(name=data).exists():
            raise forms.ValidationError(_('This character name is already taken.'))

        return data

    def clean_main_role(self):
        data = self.cleaned_data['main_role']
        game_class_id = self.data.get('game_class')

        if game_class_id:
            possible_roles = constants.CLASS_ROLE_MAPPING[models.GameClass.objects.get(id=game_class_id).name]
            possible_roles_human_readable = ', '.join(possible_roles)

            if data.name not in possible_roles:
                raise forms.ValidationError(_(f'The class you chose cannot fulfill the main role you chose. '
                                              f'Possible roles for this class are: {possible_roles_human_readable}'))

        return data

    def clean_off_spec_roles(self):
        data = self.cleaned_data['off_spec_roles']
        game_class_id = self.data.get('game_class')

        if game_class_id:
            possible_roles = constants.CLASS_ROLE_MAPPING[models.GameClass.objects.get(id=game_class_id).name]
            possible_roles_human_readable = ', '.join(possible_roles)

            for rl in data:
                if rl.name not in possible_roles:
                    raise forms.ValidationError(
                        _(f'The class you chose cannot fulfill one of the roles you chose. Possible roles for this '
                          f'class are: {possible_roles_human_readable}'))
        return data
