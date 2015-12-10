# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20150801_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionorder',
            name='start_price',
            field=models.DecimalField(default=0.0, max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(max_digits=8, decimal_places=2),
        ),
    ]
