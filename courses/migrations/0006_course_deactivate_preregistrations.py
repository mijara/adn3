# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-10 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180302_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='deactivate_preregistrations',
            field=models.BooleanField(default=False),
        ),
    ]
