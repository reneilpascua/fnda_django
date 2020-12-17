from django.contrib import admin
from .models import Position, Player, Draft, DraftPick, ZScoreSet

# Register your models here.

admin.site.register(Position)
admin.site.register(Player)
admin.site.register(ZScoreSet)
admin.site.register(Draft)
admin.site.register(DraftPick)