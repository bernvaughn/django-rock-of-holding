# Generated by Django 4.0.4 on 2022-04-20 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 20, 15, 44, 54, 853616, tzinfo=utc)),
        ),
    ]
