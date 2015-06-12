# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150612_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='creation_datetime',
            field=models.DateTimeField(default='1992-08-22', auto_now_add=True),
            preserve_default=False,
        ),
    ]
