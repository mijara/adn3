# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0012_auto_20161009_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='assistants',
            field=models.ManyToManyField(related_name='assistants', verbose_name='Ayudantes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
