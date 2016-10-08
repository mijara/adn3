# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20161008_0537'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0006_auto_20161008_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agenda', models.ForeignKey(to='courses.Agenda')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(choices=[(0, b'No asiste'), (1, b'Asiste'), (2, b'Justificado')])),
                ('attendance', models.ForeignKey(to='attendance.Attendance')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='assistants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='attendance.AttendanceShip'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='session',
            field=models.ForeignKey(to='classes.Session'),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('session', 'agenda')]),
        ),
    ]
