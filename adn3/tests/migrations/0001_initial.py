# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_session_include_assistance'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0018_auto_20161027_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('timeout', models.IntegerField(verbose_name='Duraci\xf3n', choices=[(15, '15 minutos'), (30, '30 minutos'), (45, '45 minutos'), (60, '1 hora'), (75, '1 hora 15 minutos'), (90, '1 hora 30 minutos'), (105, '1 hora 45 minutos')])),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creaci\xf3n')),
                ('show_grade', models.BooleanField(default=True, verbose_name='Mostrar nota')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('percentage', models.IntegerField(verbose_name='Porcentaje')),
                ('course', models.ForeignKey(verbose_name='Curso', to='courses.Course')),
                ('owner', models.ForeignKey(verbose_name='Due\xf1o', to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(verbose_name='Sesi\xf3n', to='classes.Session')),
            ],
        ),
    ]
