# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 13:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 22, 13, 15, 59, 289334, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 22, 13, 15, 59, 289972, tzinfo=utc)),
        ),
    ]
