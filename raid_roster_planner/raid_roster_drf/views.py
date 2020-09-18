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

        player, created = Player.objects.get_or_create(name=data['player_name'])

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
    queryset = Character.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roles_main = list(Character.objects.filter(is_main=True).values_list('role__name', flat=True).distinct())
        roles_twink = list(Character.objects.filter(is_main=False).values_list('role__name', flat=True).distinct())
        context['roles_main'] = roles_main
        context['roles_twink'] = roles_twink
        return context
