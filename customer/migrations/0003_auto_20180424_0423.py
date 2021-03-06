# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20180420_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='category',
            field=models.CharField(choices=[('structure', 'Structure'), ('particulier', 'Particulier')], default='particulier', max_length=100),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='zone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='city',
            field=models.CharField(default='abidjan', max_length=255),
        ),
    ]
