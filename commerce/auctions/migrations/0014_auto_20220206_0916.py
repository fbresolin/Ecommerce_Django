# Generated by Django 3.2.9 on 2022-02-06 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20220206_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 9, 16, 54, 838060)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid_max',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 9, 16, 54, 837060)),
        ),
    ]
