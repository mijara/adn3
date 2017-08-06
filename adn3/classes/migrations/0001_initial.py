# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-05 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('number', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32)], verbose_name='Número')),
                ('start_date', models.DateField(verbose_name='Fecha inicio')),
                ('end_date', models.DateField(verbose_name='Fecha término')),
                ('state', models.IntegerField(choices=[(0, 'Privada'), (1, 'Pública')], default=0, verbose_name='Estado')),
                ('session_type', models.IntegerField(choices=[(0, 'Regular'), (1, 'Prueba'), (2, 'Recuperativa')], default=0, verbose_name='Tipo')),
                ('include_assistance', models.BooleanField(default=True, verbose_name='Incluir en la asistencia')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='SessionFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nombre')),
                ('file', models.FileField(upload_to='', verbose_name='Archivo')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Session')),
            ],
        ),
    ]
