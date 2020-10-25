from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import FormView, ListView, TemplateView

from raid_roster_planner.raid_roster_drf import constants
from raid_roster_planner.raid_roster_drf.forms import InputForm
from raid_roster_planner.raid_roster_drf.models import Player, Character, Role


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
            main_role=data['main_role'],
            is_main=data['is_main']
        )

        for role in data['off_spec_roles'].exclude(id=data['main_role'].id):
            character.off_spec_roles.add(role)

        character.save()

        return redirect('roster')


class RosterView(ListView):
    queryset = Character.objects.all()

    def get_role_list(self, role, is_main):
        role_id = Role.objects.get(name=role).id
        return list(self.queryset.filter(is_main=is_main, main_role=role_id))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roles_main = list(Character.objects.filter(is_main=True).values_list('main_role__name', flat=True).distinct())
        roles_twink = list(Character.objects.filter(is_main=False).values_list('main_role__name', flat=True).distinct())
        context['roles_main'] = roles_main
        context['roles_twink'] = roles_twink

        context['main_tanks'] = self.get_role_list(constants.TANK, True)
        context['main_healer'] = self.get_role_list(constants.HEALER, True)
        context['main_range'] = self.get_role_list(constants.RANGED, True)
        context['main_melee'] = self.get_role_list(constants.MELEE, True)

        context['twink_tanks'] = self.get_role_list(constants.TANK, False)
        context['twink_healer'] = self.get_role_list(constants.HEALER, False)
        context['twink_range'] = self.get_role_list(constants.RANGED, False)
        context['twink_melee'] = self.get_role_list(constants.MELEE, False)

        context['amount_mains'] = self.queryset.filter(is_main=True).count()
        context['amount_twinks'] = self.queryset.filter(is_main=False).count()

        return context


def main_it(request, name):
    if request.method == 'GET':
        character = Character.objects.get(name=name)

        main_char = character.player.character_set.filter(is_main=True)
        main_char.is_main = False
        main_char.save()

        character.is_main = True
        character.save()

    html = f"<html><body>Hello {character.name}.</body></html>"
    return HttpResponse(html)

