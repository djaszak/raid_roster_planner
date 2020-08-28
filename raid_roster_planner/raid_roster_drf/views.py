from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import FormView, ListView, TemplateView

from raid_roster_planner.raid_roster_drf.forms import InputForm


class Home(TemplateView):
    template_name = 'raid_roster_drf/home.html'


class InputView(FormView):
    form_class = InputForm
    template_name = 'raid_roster_drf/input_form.html'
    success_url = reverse_lazy('roster_form')


class RosterView(ListView):
    pass
