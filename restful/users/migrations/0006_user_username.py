# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 19:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160101_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.EmailField(default=datetime.datetime(2016, 1, 1, 19, 5, 36, 824662, tzinfo=utc), max_length=254, unique=True, verbose_name='Username address'),
            preserve_default=False,
        ),
    ]
