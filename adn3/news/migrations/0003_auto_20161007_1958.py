# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20161007_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 7, 19, 58, 3, 391167, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='new',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 7, 19, 58, 8, 143430, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
