# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-06 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
        ('classes', '0001_initial'),
        ('misc', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pretest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('percentage', models.IntegerField(default=0, verbose_name='Porcentaje')),
                ('show_grade', models.BooleanField(default=False, verbose_name='Mostrar calificación')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('end_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_session', to='classes.Session', verbose_name='Sesión Entrega')),
                ('start_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_session', to='classes.Session', verbose_name='Sesión Inicio')),
            ],
        ),
        migrations.CreateModel(
            name='PretestFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to='')),
                ('pretest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pretests.Pretest')),
            ],
        ),
        migrations.CreateModel(
            name='PretestUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Archivo')),
                ('pretest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pretests.Pretest', verbose_name='Preinforme')),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc.Software', verbose_name='Software')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Student', verbose_name='Estudiante')),
            ],
        ),
    ]
