# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-02 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pretests', '0005_auto_20171002_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pretestupload',
            name='feedback',
            field=models.TextField(blank=True, null=True, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='pretestupload',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Archivo'),
        ),
        migrations.AlterField(
            model_name='pretestupload',
            name='qualification',
            field=models.IntegerField(blank=True, null=True, verbose_name='Calificación'),
        ),
        migrations.AlterField(
            model_name='pretestupload',
            name='software',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='misc.Software', verbose_name='Software'),
        ),
    ]
