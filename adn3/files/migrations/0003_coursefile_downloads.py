# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20161008_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefile',
            name='downloads',
            field=models.IntegerField(default=0, verbose_name=b'Descargas'),
        ),
    ]
