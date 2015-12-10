# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20150614_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionorder',
            name='start_price',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
        ),
    ]
