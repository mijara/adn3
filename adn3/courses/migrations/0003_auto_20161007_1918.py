# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20161007_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(choices=[(0, b'Lunes'), (1, b'Martes'), (2, b'Mi\xc3\xa9rcoles'), (3, b'Jueves'), (4, b'Viernes'), (5, b'S\xc3\xa1bado'), (6, b'Domingo')])),
                ('block', models.IntegerField(choices=[(0, b'1-2'), (1, b'3-4'), (2, b'5-6'), (3, b'7-8'), (4, b'9-10'), (5, b'11-12'), (6, b'13-14')])),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=32)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name_plural': 'Campuses'},
        ),
        migrations.AddField(
            model_name='agenda',
            name='room',
            field=models.ForeignKey(to='courses.Room'),
        ),
    ]
