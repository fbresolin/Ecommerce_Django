# Generated by Django 3.2.9 on 2022-02-06 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20220206_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bid_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 9, 14, 12, 799422)),
        ),
        migrations.AlterField(
            model_name='wish',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 9, 14, 12, 801422)),
        ),
    ]
