# Generated by Django 2.2.4 on 2019-12-26 06:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0091_auto_20191225_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='shared_point',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]