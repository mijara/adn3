# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-02 05:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preregistration', '0003_auto_20170602_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preregistration',
            name='psu_score',
        ),
    ]