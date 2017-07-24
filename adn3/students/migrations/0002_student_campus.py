# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-24 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='campus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Campus'),
            preserve_default=False,
        ),
    ]
