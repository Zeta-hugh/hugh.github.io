# Generated by Django 2.2.4 on 2019-12-23 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0069_auto_20191223_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='individual_share_a',
        ),
    ]
