# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_attendance_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attended',
            field=models.IntegerField(default=0, choices=[(0, b'No'), (1, b'Si'), (2, b'Justificado')]),
        ),
    ]
