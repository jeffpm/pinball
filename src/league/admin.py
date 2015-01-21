
from django.contrib import admin
from league.models import *

# Register your models here.

class GameInline(admin.TabularInline):
    model = Game
    extra = 0
    
class SessionInline(admin.TabularInline):
    model = Session
    extra = 1
    
class ScoreInline(admin.TabularInline):
    model = Score
    extra = 1
    
class LocationAdmin(admin.ModelAdmin):
    display = ('location_name')
    
    fieldsets = [
        (None,               {'fields': ['location_name', 'address']}),
    ]
    inlines = [GameInline]

class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'location', 'active')
    list_filter = ['active']
    
    def location(self, instance):
        return instance.location.location_name

class SeasonAdmin(admin.ModelAdmin):
    list_display =('season_name', 'active')
    inlines = [SessionInline]
    
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'ifpa_number')
    
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('session', 'player', 'game', 'score')
    
    def session(self, instance):
        return instance.session.session_name
    def player(self, instance):
        return instance.player.player_name
    def game(self, instance):
        return instance.game.game_name
    
class SessionAdmin(admin.ModelAdmin):
    list_display = ('season',  'session_number','session_date', 'location')
    inlines = [ScoreInline]
    
    def season(self, instance):
        return instance.season.season_name
    def location(self, instance):
        return instance.location.location_name
   
admin.site.register(Location,LocationAdmin)
admin.site.register(Game,GameAdmin)
admin.site.register(Season,SeasonAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(Score,ScoreAdmin)
admin.site.register(Session,SessionAdmin)