# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_coursefile_downloads'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 8, 15, 19, 45, 388447, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursefile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 8, 15, 19, 49, 756577, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
