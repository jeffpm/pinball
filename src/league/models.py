from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.location_name
    
class Game(models.Model):
    game_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.game_name
    
class Season(models.Model):
    season_name = models.CharField(max_length=100)
    def __str__(self):
        return self.season_name
    
class Session(models.Model):
    session_date = models.DateField('session date')
    session_number = models.IntegerField()
    season = models.ForeignKey(Season)
    location = models.ForeignKey(Location)
    def __str__(self):
        return self.session_date

class Player(models.Model):
    player_name = models.CharField(max_length=100)
    ifpa_number = models.IntegerField(default=0)
    def __str__(self):
        return self.player_name
    
class Score(models.Model):
    score = models.BigIntegerField()
    player = models.ForeignKey(Player)
    game = models.ForeignKey(Game)
    session = models.ForeignKey(Session)
    def __str__(self):
        return self.score
    
class Group(models.Model):
    group_name = models.CharField(max_length=50)
    player = models.ForeignKey(Player)
    session = models.ForeignKey(Session)
    def __str__(self):
        return self.group_name