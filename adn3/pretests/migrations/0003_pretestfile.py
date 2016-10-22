# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pretests', '0002_pretest_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='PretestFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to=b'')),
                ('pretest', models.ForeignKey(to='pretests.Pretest')),
            ],
        ),
    ]
