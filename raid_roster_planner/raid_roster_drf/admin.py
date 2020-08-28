from django.contrib import admin

from .models import Character
from .models import GameClass
from .models import Player
from .models import Role


# Register your models here.

admin.site.register(Character)
admin.site.register(GameClass)
admin.site.register(Player)
admin.site.register(Role)
