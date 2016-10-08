# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_remove_class_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ('number',)},
        ),
    ]
