# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150613_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionorder',
            name='start_price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='bet',
            name='amount',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='auction_percent',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='order_percent',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
