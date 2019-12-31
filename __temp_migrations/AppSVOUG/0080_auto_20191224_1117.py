# Generated by Django 2.2.4 on 2019-12-24 03:17

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0079_fsvo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='fsvo',
        ),
        migrations.RemoveField(
            model_name='player',
            name='accept_offer',
        ),
        migrations.AlterField(
            model_name='player',
            name='offer_accept',
            field=otree.db.models.IntegerField(choices=[[1, '接受'], [0, '不接受']], null=True, verbose_name='你是否接受这个方案?'),
        ),
    ]
