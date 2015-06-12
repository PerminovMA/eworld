# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150612_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'FINDING_MANAGER', max_length=16, choices=[(b'FINDING_MANAGER', b'Finding event manager'), (b'FOUND_MANAGER', b'Event manager found'), (b'ORDER_IN_PROCESS', b'Order in process'), (b'ORDER_COMPLETE', b'Order complete')]),
        ),
    ]
