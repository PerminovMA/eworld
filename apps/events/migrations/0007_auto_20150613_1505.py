# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_remove_auctionorder_bets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionorder',
            name='categories',
            field=models.ManyToManyField(related_name='auctionorder_set', to='events.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='categories',
            field=models.ManyToManyField(related_name='order_set', to='events.Category', blank=True),
        ),
    ]
