# Generated by Django 2.2.4 on 2019-12-22 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0061_auto_20191222_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsession',
            name='fake_svo_angle',
        ),
        migrations.RemoveField(
            model_name='subsession',
            name='individual_share_a',
        ),
        migrations.RemoveField(
            model_name='subsession',
            name='shared_point',
        ),
        migrations.RemoveField(
            model_name='subsession',
            name='slider_angle',
        ),
        migrations.RemoveField(
            model_name='subsession',
            name='slider_classification',
        ),
    ]
