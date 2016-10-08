# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendanceship',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='attendanceship',
            name='user',
        ),
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('session', 'agenda', 'user')]),
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='assistants',
        ),
        migrations.DeleteModel(
            name='AttendanceShip',
        ),
    ]
