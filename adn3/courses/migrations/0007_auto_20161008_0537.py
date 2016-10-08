# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0006_auto_20161008_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='agenda',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='user',
        ),
        migrations.AddField(
            model_name='agenda',
            name='inscriptions',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Inscription',
        ),
    ]
