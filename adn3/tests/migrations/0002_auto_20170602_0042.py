# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-02 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='file',
            field=models.FileField(blank=True, upload_to='tests/'),
        ),
        migrations.AlterField(
            model_name='version',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Test', verbose_name='Control'),
        ),
    ]