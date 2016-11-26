# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 15:24
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0008_session_include_assistance'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('misc', '0001_initial'),
        ('courses', '0018_auto_20161027_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(verbose_name='\xcdndice')),
                ('text', models.TextField(verbose_name='Texto')),
                ('correct', models.BooleanField(default=False, verbose_name='Es correcta')),
            ],
            options={
                'ordering': ('index',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Enunciado')),
                ('score', models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Puntaje')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('timeout', models.IntegerField(choices=[(15, '15 minutos'), (30, '30 minutos'), (45, '45 minutos'), (60, '1 hora'), (75, '1 hora 15 minutos'), (90, '1 hora 30 minutos'), (105, '1 hora 45 minutos')], verbose_name='Duraci\xf3n')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creaci\xf3n')),
                ('show_grade', models.BooleanField(default=True, verbose_name='Mostrar nota')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('percentage', models.IntegerField(verbose_name='Porcentaje')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Curso')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Due\xf1o')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Session', verbose_name='Sesi\xf3n')),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc.Software', verbose_name='Software')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Test', verbose_name=b'Control')),
            ],
            options={
                'verbose_name': 'Forma',
                'verbose_name_plural': 'Formas',
            },
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tests.Question')),
            ],
            bases=('tests.question',),
        ),
        migrations.AddField(
            model_name='question',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Version', verbose_name=b'Forma'),
        ),
        migrations.AddField(
            model_name='alternative',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.ChoiceQuestion'),
        ),
    ]