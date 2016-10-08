# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_inscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='course',
        ),
        migrations.AddField(
            model_name='inscription',
            name='agenda',
            field=models.ForeignKey(default=1, to='courses.Agenda'),
            preserve_default=False,
        ),
    ]
