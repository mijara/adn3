# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pretests', '0003_pretestfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pretest',
            name='end_session',
            field=models.ForeignKey(related_name='end_session', verbose_name='Sesi\xf3n Entrega', to='classes.Session'),
        ),
        migrations.AlterField(
            model_name='pretest',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='pretest',
            name='percentage',
            field=models.FloatField(default=0, verbose_name='Porcentaje'),
        ),
        migrations.AlterField(
            model_name='pretest',
            name='show_grade',
            field=models.BooleanField(default=False, verbose_name='Mostrar calificaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='pretest',
            name='start_session',
            field=models.ForeignKey(related_name='start_session', verbose_name='Sesi\xf3n Inicio', to='classes.Session'),
        ),
    ]
