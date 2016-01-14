# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionorder',
            name='comments',
            field=models.ManyToManyField(to='events.Comment', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='comments',
            field=models.ManyToManyField(to='events.Comment', blank=True),
        ),
    ]
