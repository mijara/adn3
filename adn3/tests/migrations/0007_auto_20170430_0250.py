# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-30 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_question_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='html',
            field=models.TextField(editable=False, verbose_name='html'),
        ),
    ]
