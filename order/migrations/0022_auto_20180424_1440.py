# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 13:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20180424_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 24, 14, 40, 26, 92567), null=True),
        ),
    ]
