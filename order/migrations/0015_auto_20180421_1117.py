# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 10:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20180421_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 21, 11, 17, 20, 12443), null=True),
        ),
    ]
