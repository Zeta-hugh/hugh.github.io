# Generated by Django 2.2.4 on 2019-12-22 08:12

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0063_auto_20191222_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='shared_point',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
