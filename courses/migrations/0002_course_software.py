# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-04 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='software',
            field=models.ManyToManyField(to='misc.Software', verbose_name='Software'),
        ),
    ]
