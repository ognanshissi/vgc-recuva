# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 14:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0036_auto_20180507_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 5, 7, 15, 1, 26, 871232), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipped_at',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]