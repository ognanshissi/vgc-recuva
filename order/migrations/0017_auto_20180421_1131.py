# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 10:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20180421_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 21, 11, 31, 34, 700587), null=True),
        ),
    ]