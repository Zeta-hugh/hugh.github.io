# Generated by Django 2.2.4 on 2019-12-22 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0057_auto_20191222_1338'),
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
        migrations.RemoveField(
            model_name='player',
            name='slider_angle',
        ),
        migrations.RemoveField(
            model_name='player',
            name='slider_classification',
        ),
    ]
