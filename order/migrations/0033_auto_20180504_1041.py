# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 09:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20180504_1041'),
        ('order', '0032_auto_20180503_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zone',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='customer.GroupZone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='advance',
            field=models.DecimalField(decimal_places=2, default=5000.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='mount',
            field=models.CharField(choices=[('rayban classic', 'RayBan Classic'), ('rayban', 'RayBan'), ('chat', 'Chat')], default='rayban classic', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 4, 10, 41, 9, 283736), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, default=60000.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='rest',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
