# Generated by Django 2.2.4 on 2019-12-23 09:26

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0076_auto_20191223_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='shared_point',
            field=otree.db.models.CurrencyField(null=True),
        ),
    ]
