# Generated by Django 2.2.4 on 2019-12-20 07:06

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0008_auto_20191220_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='fake_svo_angle',
            field=otree.db.models.FloatField(default=10.04, null=True),
        ),
    ]
