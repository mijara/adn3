# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-24 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_software'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='code',
            field=models.CharField(max_length=64, null=True, verbose_name='Código de inscripción'),
        ),
    ]
