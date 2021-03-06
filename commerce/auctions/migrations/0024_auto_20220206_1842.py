# Generated by Django 3.2.9 on 2022-02-06 21:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20220206_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bid_count',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='bid_max',
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 21, 42, 17, 678476, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bid',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 21, 42, 17, 677476, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 21, 42, 17, 676478, tzinfo=utc)),
        ),
    ]
