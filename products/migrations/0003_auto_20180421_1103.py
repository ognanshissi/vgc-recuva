# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-21 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180421_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='axe',
            field=models.CharField(choices=[('None', "selectionnez l'axe la lentille"), ('90', '90°'), ('110', '110°'), ('180', '180°')], default=None, max_length=4),
        ),
    ]