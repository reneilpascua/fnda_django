from django.db import models
from draft_assistant import settings

# Create your models here.

class Position(models.Model):
    '''
    A position which can be used to categorize a player
    '''
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    '''
    A player to be picked, with projected stats.
    These stats are for 2020-2021 season from
    https://www.fantasypros.com/nba/projections/overall.php
    '''

    # identification
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=3)
    positions = models.ManyToManyField(Position)
    
    # stats
    points = models.IntegerField()
    rebounds = models.IntegerField()
    assists = models.IntegerField()
    blocks = models.IntegerField()
    steals = models.IntegerField()
    fg_pct = models.FloatField()
    ft_pct = models.FloatField()
    threes = models.IntegerField()
    games_played = models.IntegerField()
    minutes = models.IntegerField()
    turnovers = models.IntegerField()

    # projected draft positions
    rank = models.IntegerField()
    avg_rank = models.FloatField()

    def __str__(self):
        return f'{self.name} ({self.team})'

class ZScoreSet(models.Model):
    '''
    Represent's a player's Z scores as opposed to their raw stats
    '''
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    pointsZ = models.FloatField()
    reboundsZ = models.FloatField()
    assistsZ = models.FloatField()
    blocksZ = models.FloatField()
    stealsZ = models.FloatField()
    fg_pctZ = models.FloatField()
    ft_pctZ = models.FloatField()
    threesZ = models.FloatField()
    turnoversZ = models.FloatField()

    def __str__(self):
        return f'{self.player.name}\'s z-scores'

class Draft(models.Model):
    '''
    A (mock) draft created by a user
    '''
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} by {self.creator}'

class DraftPick(models.Model):
    '''
    A player pick, whether belonging to the user initiating the draft, or someone else.
    '''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    draft = models.ForeignKey(Draft, on_delete=models.CASCADE)
    round_picked = models.IntegerField()
    round_place = models.IntegerField(null=True)
    overall_place = models.IntegerField()

    def __str__(self):
        return f'[Draft ID {self.draft.id}]{self.player.name} by {self.owner} ({self.overall_place})'