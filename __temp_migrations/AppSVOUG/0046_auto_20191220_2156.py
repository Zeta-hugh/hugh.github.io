# Generated by Django 2.2.4 on 2019-12-20 13:56

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSVOUG', '0045_auto_20191220_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='gfeeling_rating',
            field=otree.db.models.IntegerField(choices=[[1, '轻微不开心'], [1, '有点不开心'], [1, ''], [1, '接受'], [1, '非常不开心']], null=True, verbose_name='你是否接受这个方案?'),
        ),
    ]
