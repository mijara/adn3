# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='content',
        ),
        migrations.AddField(
            model_name='new',
            name='body',
            field=models.TextField(default='', verbose_name='Cuerpo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new',
            name='course',
            field=models.ForeignKey(verbose_name='Curso', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=512, verbose_name='T\xedtulo'),
        ),
    ]
