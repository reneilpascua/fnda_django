from django.core.management.base import BaseCommand, CommandError
from assistant.models import Player, Position
import csv

class Command(BaseCommand):
    help = 'imports players into the database'

    def handle(self, *args, **options):

        # make csv reader and skip first row
        f = open('./csvs/FantasyPros_Fantasy_Basketball_Overall_2020_Projections_0.csv')
        reader = csv.reader(f)
        next(reader)

        # create (or get) objects
        for row in reader:
            
            player, created = Player.objects.get_or_create(
                name = row[0],
                team = row[1],

                points = int(float(row[3])),
                rebounds = row[4],
                assists = row[5],
                blocks = row[6],
                steals = row[7],
                fg_pct = row[8],
                ft_pct = row[9],
                threes = row[10],
                games_played = row[11],
                minutes = int(float(row[12])),
                turnovers = row[13],    
            )
            
            poses = (row[2]).split(',')
            print(f'{player.name} positions: {poses}')
            for pos in poses:
                pos_obj = Position.objects.filter(name=pos).first()
                player.positions.add(pos_obj)

        f.close()
