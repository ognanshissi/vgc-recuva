# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 09:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_auto_20180425_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 25, 10, 30, 44, 346956), null=True),
        ),
    ]
