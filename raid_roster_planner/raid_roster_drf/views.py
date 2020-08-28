from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, ListView, TemplateView


class Home(TemplateView):
    template_name = 'raid_roster_drf/home.html'

    pass


class InputView(FormView):
    pass


class RosterView(ListView):
    pass
