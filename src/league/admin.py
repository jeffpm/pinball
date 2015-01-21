
from django.contrib import admin
from league.models import *

# Register your models here.

class GameInline(admin.TabularInline):
    model = Game
    extra = 0
    
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

   
admin.site.register(Location,LocationAdmin)
admin.site.register(Game,GameAdmin)