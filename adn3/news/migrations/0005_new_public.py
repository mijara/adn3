# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_new_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='public',
            field=models.BooleanField(default=False, help_text='Si es p\xfablico, adem\xe1s, se mostrar\xe1 en el iniciopara usuarios sin iniciar sesi\xf3n.', verbose_name='P\xfablico'),
        ),
    ]
