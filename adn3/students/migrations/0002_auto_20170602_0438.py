# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-02 04:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rol',
            field=models.CharField(max_length=20, verbose_name='Rol USM'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='student',
            name='usm_priority',
            field=models.IntegerField(verbose_name='Prioridad'),
        ),
    ]