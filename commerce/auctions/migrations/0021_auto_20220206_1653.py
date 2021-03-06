# Generated by Django 3.2.9 on 2022-02-06 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auto_20220206_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bid_user',
            field=models.CharField(default='admin', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 19, 53, 32, 535357, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 19, 53, 32, 534359, tzinfo=utc)),
        ),
    ]
