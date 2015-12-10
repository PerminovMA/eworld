# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20150929_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionorder',
            name='min_price',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True),
        ),
    ]
