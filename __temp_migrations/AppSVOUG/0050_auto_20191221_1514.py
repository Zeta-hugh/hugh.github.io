# Generated by Django 2.2.4 on 2019-12-21 07:14

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0049_auto_20191221_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='accept_offer',
        ),
        migrations.AddField(
            model_name='player',
            name='offer_accept',
            field=otree.db.models.BooleanField(choices=[[True, '接受'], [False, '不接受']], null=True, verbose_name='你是否接受这个方案?'),
        ),
    ]