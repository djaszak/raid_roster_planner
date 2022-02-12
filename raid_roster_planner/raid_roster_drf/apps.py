from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RaidRosterDrfConfig(AppConfig):
    name = 'raid_roster_planner.raid_roster_drf'
    verbose_name = _('Roster Planner')
