# Generated by Django 2.2.4 on 2019-12-23 02:27

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0066_auto_20191222_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='fake_svo_angle',
        ),
        migrations.RemoveField(
            model_name='player',
            name='individual_share_a',
        ),
        migrations.RemoveField(
            model_name='player',
            name='shared_point',
        ),
        migrations.AddField(
            model_name='group',
            name='fake_svo_angle',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='individual_share_a',
            field=otree.db.models.CurrencyField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='shared_point',
            field=otree.db.models.CurrencyField(null=True),
        ),
    ]
