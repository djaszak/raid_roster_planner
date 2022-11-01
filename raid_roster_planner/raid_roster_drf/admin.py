from django.contrib import admin

from .forms.admin import GameClassAdminForm
from .models import Character, GameClass, Player, Role


class GameClassAdmin(admin.ModelAdmin):
    form = GameClassAdminForm


admin.site.register(Character)
admin.site.register(GameClass, GameClassAdmin)
admin.site.register(Player)
admin.site.register(Role)
