# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_agenda_assistants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='inscriptions',
            field=models.ManyToManyField(related_name='inscriptions', verbose_name='Inscritos', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
