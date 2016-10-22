# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_sessionfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pretest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('percentage', models.FloatField(default=0)),
                ('show_grade', models.BooleanField(default=False)),
                ('end_session', models.ForeignKey(related_name='end_session', to='classes.Session')),
                ('start_session', models.ForeignKey(related_name='start_session', to='classes.Session')),
            ],
        ),
    ]
