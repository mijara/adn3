# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20161010_0201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name_plural': 'Campus'},
        ),
    ]
