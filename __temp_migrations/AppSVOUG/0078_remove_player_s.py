# Generated by Django 2.2.4 on 2019-12-23 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0077_player_shared_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='s',
        ),
    ]
