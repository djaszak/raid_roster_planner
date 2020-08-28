from django.shortcuts import render

from django.views.generic import FormView, ListView, TemplateView

from raid_roster_planner.raid_roster_drf.forms import InputForm


class Home(TemplateView):
    template_name = 'raid_roster_drf/home.html'

    pass


class InputView(FormView):
    form_class = InputForm
    template_name = 'raid_roster_drf/placeholder.html'


class RosterView(ListView):
    pass
