# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 11:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_auto_20180425_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 25, 12, 35, 38, 178272), null=True),
        ),
    ]