# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-06 05:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attended', models.IntegerField(choices=[(0, 'No'), (1, 'Si'), (2, 'Justificado')], default=0)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Agenda')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('session', 'agenda', 'user')]),
        ),
    ]
