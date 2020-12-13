# Generated by Django 3.1.4 on 2020-12-13 22:15

from django.db import migrations
import csv

def create_positions(apps, schema_editor):
    Position = apps.get_model('assistant', 'Position')
    available_positions = ['PG','SG','PF','SF','C']
    for pos in available_positions:
        Position.objects.create(
            name = pos
        )

def import_players(apps, schema_editor):
    Player = apps.get_model('assistant', 'Player')
    Position = apps.get_model('assistant', 'Position')
    
    # make csv reader and skip first row
    f = open('./csvs/FantasyPros_Fantasy_Basketball_Overall_2020_Projections_0.csv')
    reader = csv.reader(f)
    next(reader)

    # create (or get) objects
    for row in reader:
        
        player, created = Player.objects.get_or_create(
            name = row[0],
            team = row[1],

            points = int(row[3]),
            rebounds = row[4],
            assists = row[5],
            blocks = row[6],
            steals = row[7],
            fg_pct = row[8],
            ft_pct = row[9],
            threes = row[10],
            games_played = row[11],
            minutes = int(row[12]),
            turnovers = row[13],
            rank = row[14],
            avg_rank = row[15]
        )
        
        poses = (row[2]).split(',')
        for pos in poses:
            pos_obj = Position.objects.filter(name=pos).first()
            player.positions.add(pos_obj)

    f.close()

class Migration(migrations.Migration):
    '''
    seeding the positions!
    '''
    dependencies = [
        ('assistant', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_positions),
        migrations.RunPython(import_players),
    ]