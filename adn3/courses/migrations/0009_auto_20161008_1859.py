# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20161008_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='inscriptions',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Inscripciones', blank=True),
        ),
    ]
