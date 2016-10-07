# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'Nombre')),
                ('code', models.CharField(max_length=16, verbose_name=b'Sigla')),
                ('semester', models.IntegerField(verbose_name=b'Semestre', choices=[(1, 1), (2, 2)])),
                ('year', models.IntegerField(verbose_name=b'A\xc3\xb1o', choices=[(2015, 2015), (2016, 2016)])),
                ('status', models.BooleanField(default=True, verbose_name=b'Estado')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
