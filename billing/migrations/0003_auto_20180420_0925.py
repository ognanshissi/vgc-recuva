# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20180420_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='paid_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]