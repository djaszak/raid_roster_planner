from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import FormView, ListView, TemplateView

from raid_roster_planner.raid_roster_drf.forms import InputForm
from raid_roster_planner.raid_roster_drf.models import Player, Character


class Home(TemplateView):
    template_name = 'raid_roster_drf/home.html'


class InputView(FormView):
    form_class = InputForm
    template_name = 'raid_roster_drf/input_form.html'
    success_url = reverse_lazy('roster_form')

    def form_valid(self, form):
        data = form.cleaned_data

        player = Player.objects.create(name=data['player_name'])

        character = Character.objects.create(
            name=data['character_name'],
            player=player,
            game_class=data['game_class'],
            is_main=data['is_main'],
        )

        for role in data['role']:
            character.role.add(role)

        character.save()

        return redirect('roster')


class RosterView(ListView):
    pass
