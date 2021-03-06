# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_billings', to='order.Order'),
        ),
        migrations.AlterField(
            model_name='billing',
            name='paid_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='billing',
            name='payment_due',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='billing',
            name='status',
            field=models.CharField(choices=[('Paid', 'Soldé'), ('Late', 'Retard'), ('Pending', 'En Attente')], default='Pending', max_length=100),
        ),
    ]
