# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 13:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('due', models.DateTimeField()),
                ('calculated_due', models.DateTimeField()),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 22, 13, 14, 58, 633842))),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 10, 22, 13, 14, 58, 634434))),
                ('due', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Project')),
            ],
        ),
    ]
