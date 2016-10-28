# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_sessionfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='include_assistance',
            field=models.BooleanField(default=True, verbose_name='Incluir en la asistencia'),
        ),
    ]
