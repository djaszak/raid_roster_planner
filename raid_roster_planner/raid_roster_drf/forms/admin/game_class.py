from django import forms

from raid_roster_planner.raid_roster_drf.models import GameClass


class GameClassAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = GameClass
        widgets = {
            'colour': forms.TextInput(attrs={'type': 'color'}),
        }
