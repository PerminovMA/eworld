# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_bet_creation_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionorder',
            name='bets',
            field=models.ManyToManyField(to='events.Bet', blank=True),
        ),
    ]
