# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-14 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='html',
            field=models.TextField(default='<h1>noticias :D </h1', verbose_name='Html'),
            preserve_default=False,
        ),
    ]
