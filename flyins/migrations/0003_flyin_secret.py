# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-08 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyins', '0002_auto_20170907_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyin',
            name='secret',
            field=models.CharField(default='NULL', max_length=64),
            preserve_default=False,
        ),
    ]
