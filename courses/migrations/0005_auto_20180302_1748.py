# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-02 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170925_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[(2017, 2017), (2018, 2018)], verbose_name='Año'),
        ),
    ]
