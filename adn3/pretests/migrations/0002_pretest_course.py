# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20161022_2243'),
        ('pretests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pretest',
            name='course',
            field=models.ForeignKey(default=1, to='courses.Course'),
            preserve_default=False,
        ),
    ]
