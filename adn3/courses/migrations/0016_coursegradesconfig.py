# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20161022_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGradesConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade_tests', models.FloatField(verbose_name='% Nota controles')),
                ('grade_pretests', models.FloatField(verbose_name='% Nota preinformes')),
                ('grade_assistance', models.FloatField(verbose_name='% Nota asistencia')),
                ('show_final_grade', models.FloatField(verbose_name='Mostrar nota final')),
                ('course', models.OneToOneField(related_name='grades_config', blank=True, to='courses.Course')),
            ],
        ),
    ]
