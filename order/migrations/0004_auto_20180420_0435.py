# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20180420_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='month_to_pay',
        ),
        migrations.AlterField(
            model_name='order',
            name='scheduled_shipped_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]