# Generated by Django 2.2.4 on 2019-12-22 08:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0064_player_shared_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slider_angle',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]