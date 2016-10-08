# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20161008_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='block',
            field=models.IntegerField(verbose_name='Bloque', choices=[(0, b'1-2'), (1, b'3-4'), (2, b'5-6'), (3, b'7-8'), (4, b'9-10'), (5, b'11-12'), (6, b'13-14')]),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='course',
            field=models.ForeignKey(verbose_name='Curso', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='day',
            field=models.IntegerField(verbose_name='D\xeda', choices=[(0, b'Lunes'), (1, b'Martes'), (2, b'Mi\xc3\xa9rcoles'), (3, b'Jueves'), (4, b'Viernes'), (5, b'S\xc3\xa1bado'), (6, b'Domingo')]),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='inscriptions',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Inscripciones'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='room',
            field=models.ForeignKey(verbose_name='Sala', to='courses.Room'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(max_length=32, verbose_name='C\xf3digo'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='room',
            name='seats',
            field=models.IntegerField(verbose_name='Asientos'),
        ),
    ]
