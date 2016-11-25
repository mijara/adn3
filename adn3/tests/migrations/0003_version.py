# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_test_software'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(verbose_name=b'Control', to='tests.Test')),
            ],
            options={
                'verbose_name': 'Forma',
                'verbose_name_plural': 'Formas',
            },
        ),
    ]
