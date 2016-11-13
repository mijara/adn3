# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='software',
            field=models.ForeignKey(default=1, verbose_name='Software', to='misc.Software'),
            preserve_default=False,
        ),
    ]
