# Generated by Django 4.0.2 on 2022-02-21 21:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantedtree',
            name='planted_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 2, 21, 21, 58, 16, 430546, tzinfo=utc)),
            preserve_default=False,
        ),
    ]