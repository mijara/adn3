# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-08 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyins', '0003_flyin_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyin',
            name='seen_details',
            field=models.BooleanField(default=False),
        ),
    ]