# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='inscriptions',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Inscritos', blank=True),
        ),
    ]
