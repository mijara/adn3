# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-30 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preregistration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preregistration',
            name='psu_score',
            field=models.IntegerField(help_text='Para alumnos de primer a\xf1o', null=True, verbose_name='Puntaje PSU'),
        ),
    ]
