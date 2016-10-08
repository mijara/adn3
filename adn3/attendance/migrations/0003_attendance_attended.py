# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20161008_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='attended',
            field=models.IntegerField(default=1, choices=[(0, b'No'), (1, b'Si'), (2, b'Justificado')]),
            preserve_default=False,
        ),
    ]
