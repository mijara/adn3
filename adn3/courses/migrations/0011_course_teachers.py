# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0010_auto_20161009_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Profesores', through='courses.CourseTeacher', blank=True),
        ),
    ]
