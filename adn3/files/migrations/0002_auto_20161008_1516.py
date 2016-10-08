# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefile',
            name='name',
            field=models.CharField(default='Un Archivo', max_length=256, verbose_name=b'Nombre'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursefile',
            name='file',
            field=models.FileField(upload_to=b'', verbose_name=b'Archivo'),
        ),
    ]
