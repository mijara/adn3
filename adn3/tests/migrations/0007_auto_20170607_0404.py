# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-07 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20170603_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choiceanswer',
            old_name='choiceQuestion',
            new_name='choice_question',
        ),
        migrations.RenameField(
            model_name='numericalanswer',
            old_name='numericalQuestion',
            new_name='numerical_question',
        ),
        migrations.RenameField(
            model_name='textanswer',
            old_name='textQuestion',
            new_name='text_question',
        ),
        migrations.AddField(
            model_name='studentsanswers',
            name='submitted',
            field=models.BooleanField(default=False, verbose_name='Enviado'),
        ),
    ]
