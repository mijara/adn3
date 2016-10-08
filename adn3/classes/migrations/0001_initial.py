# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20161008_0537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('number', models.IntegerField(verbose_name='N\xfamero', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32)])),
                ('start_date', models.DateField(verbose_name='Fecha inicio')),
                ('end_date', models.DateField(verbose_name='Fecha t\xe9rmino')),
                ('duration', models.IntegerField(verbose_name='Duraci\xf3n')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
    ]
