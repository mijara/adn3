# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-05 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20170816_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('pk',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('pk',)},
        ),
    ]
