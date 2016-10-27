# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_new_public'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ('-create_date',)},
        ),
        migrations.AlterField(
            model_name='new',
            name='public',
            field=models.BooleanField(default=False, help_text='Si es p\xfablico, adem\xe1s, se mostrar\xe1 en el inicio para usuarios sin iniciar sesi\xf3n.', verbose_name='P\xfablico'),
        ),
    ]
