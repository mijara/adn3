# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20161007_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(verbose_name='A\xf1o', choices=[(2015, 2015), (2016, 2016)]),
        ),
    ]
