# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20180420_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='billing_order',
            field=models.PositiveSmallIntegerField(default=1, editable=False),
        ),
    ]
