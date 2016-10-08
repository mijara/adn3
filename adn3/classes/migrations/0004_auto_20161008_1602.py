# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20161008_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='session_type',
            field=models.IntegerField(default=0, choices=[(0, b'Regular'), (1, b'Prueba'), (2, b'Recuperativa')]),
        ),
        migrations.AddField(
            model_name='class',
            name='state',
            field=models.IntegerField(default=0, choices=[(0, b'Privada'), (1, b'P\xc3\xbablica')]),
        ),
    ]
