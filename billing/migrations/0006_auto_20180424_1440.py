# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_auto_20180420_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billing',
            options={'ordering': ['billing_order']},
        ),
        migrations.AlterField(
            model_name='billing',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
    ]
