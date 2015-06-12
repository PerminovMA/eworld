# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_bet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('order_percent', models.FloatField()),
                ('auction_percent', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='auctionorder',
            name='categories',
            field=models.ManyToManyField(related_name='auctionorder_categories_set', to='events.Category', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='categories',
            field=models.ManyToManyField(related_name='order_categories_set', to='events.Category', blank=True),
        ),
    ]
