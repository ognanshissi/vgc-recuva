# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20180425_1015'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerAddress',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='zone',
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
