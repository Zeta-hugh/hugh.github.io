# Generated by Django 2.2.4 on 2019-12-25 10:15

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0090_auto_20191225_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='fake_svo_angle',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
