# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20161027_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegradesconfig',
            name='show_final_grade',
            field=models.BooleanField(default=True, verbose_name='Mostrar nota final'),
        ),
    ]
