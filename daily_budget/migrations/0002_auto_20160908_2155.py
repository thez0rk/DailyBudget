# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]