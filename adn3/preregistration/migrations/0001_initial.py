# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-30 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0019_auto_20170207_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Nombre')),
                ('last_names', models.CharField(max_length=256, verbose_name='Apellidos')),
                ('usm_rol', models.CharField(max_length=12, verbose_name='Rol USM')),
                ('usm_priority', models.IntegerField(verbose_name='Prioridad USM')),
                ('psu_score', models.IntegerField(help_text='Para alumnos de primer a\xf1o', verbose_name='Puntaje PSU')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('first_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='courses.Agenda', verbose_name='Primera Preferencia')),
                ('second_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second', to='courses.Agenda', verbose_name='Segunda Preferencia')),
                ('third_preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third', to='courses.Agenda', verbose_name='Tercera Preferencia')),
            ],
        ),
    ]
