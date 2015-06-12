# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auctionorder_bets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionorder',
            name='bets',
        ),
    ]
