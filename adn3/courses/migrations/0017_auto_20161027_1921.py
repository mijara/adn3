# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_coursegradesconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegradesconfig',
            name='course',
            field=models.OneToOneField(related_name='grades_config', null=True, blank=True, to='courses.Course'),
        ),
    ]
