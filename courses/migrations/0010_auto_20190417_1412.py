# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-04-17 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20180411_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[(2018, 2018), (2019, 2019)], verbose_name='Año'),
        ),
    ]
