# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 09:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20180420_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 21, 10, 57, 54, 921290), null=True),
        ),
    ]
