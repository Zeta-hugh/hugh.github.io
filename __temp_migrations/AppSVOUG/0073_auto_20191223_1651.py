# Generated by Django 2.2.4 on 2019-12-23 08:51

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0072_auto_20191223_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='slider1',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider2',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider3',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider4',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider5',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='slider6',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]