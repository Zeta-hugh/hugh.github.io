# Generated by Django 2.2.4 on 2019-12-21 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0050_auto_20191221_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='s',
        ),
    ]
