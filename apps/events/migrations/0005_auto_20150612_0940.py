# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150612_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionorder',
            name='requirements',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='requirements',
            field=models.TextField(null=True, blank=True),
        ),
    ]
