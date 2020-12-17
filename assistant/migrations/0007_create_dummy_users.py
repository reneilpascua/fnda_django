# Generated by Django 3.1.4 on 2020-12-17 17:11

from django.db import migrations
from django.contrib.auth.models import User

def create_dummies(apps, schema_editor):
    
    for i in range(14):
        User.objects.create(
            id=100+i,
            username=f'User {i+1}',
            password='djang0SecretKey'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0006_auto_20201217_1711'),
    ]

    operations = [
        migrations.RunPython(create_dummies)
    ]
