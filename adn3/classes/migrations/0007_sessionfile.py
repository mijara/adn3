# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_auto_20161008_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'Nombre')),
                ('file', models.FileField(upload_to=b'', verbose_name=b'Archivo')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(to='classes.Session')),
            ],
        ),
    ]
