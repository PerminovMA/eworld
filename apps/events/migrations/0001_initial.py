# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField()),
                ('requirements', models.TextField(null=True, blank=True)),
                ('start_price', models.FloatField()),
                ('status', models.CharField(max_length=18, choices=[(b'AUCTION_IN_PROCESS', b'auction in process'), (b'MANAGER_SELECTING', b'manager_selecting'), (b'MANAGER_SELECTED', b'manager_selected'), (b'ORDER_IN_PROCESS', b'order_in_process'), (b'ORDER_COMPLETE', b'ORDER_COMPLETE')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('order_percent', models.FloatField()),
                ('auction_percent', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField()),
                ('requirements', models.TextField(null=True, blank=True)),
                ('status', models.CharField(max_length=16, choices=[(b'FINDING_MANAGER', b'Finding event manager'), (b'FOUND_MANAGER', b'Event manager found'), (b'ORDER_IN_PROCESS', b'Order in process'), (b'ORDER_COMPLETE', b'Order complete')])),
                ('price', models.FloatField()),
                ('categories', models.ManyToManyField(related_name='order_categories_set', to='events.Category', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
