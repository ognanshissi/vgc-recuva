# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 09:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20180425_1015'),
        ('order', '0023_auto_20180424_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='commercial_group',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='customer.Group'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 25, 10, 15, 40, 716234), null=True),
        ),
    ]