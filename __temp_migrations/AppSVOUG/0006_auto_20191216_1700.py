# Generated by Django 2.2.4 on 2019-12-16 09:00

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0005_auto_20191216_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='accept_offer',
            field=otree.db.models.BooleanField(choices=[[True, '接受'], [False, '不接受']], null=True, verbose_name='你是否接受这个方案?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='offer_amount',
            field=otree.db.models.CurrencyField(null=True, verbose_name='你愿意分配给玩家B多少点数？'),
        ),
    ]
