# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 03:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('sphere', models.FloatField(blank=True, default=0.0, null=True)),
                ('cylindre', models.FloatField(blank=True, default=0.0, null=True)),
                ('axe', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('addition', models.PositiveSmallIntegerField(blank=True, default=0.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Type'),
        ),
    ]
