# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0009_auto_20161008_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTeacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coordinates', models.BooleanField(verbose_name='Coordinador')),
                ('course', models.ForeignKey(verbose_name=b'Curso', to='courses.Course')),
                ('user', models.ForeignKey(verbose_name=b'Profesor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
