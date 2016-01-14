# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20151217_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 22, 11, 9, 807124, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
