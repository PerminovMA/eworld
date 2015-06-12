# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('events', '0002_auto_20150611_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('auction', models.ForeignKey(to='events.AuctionOrder')),
                ('owner', models.ForeignKey(to='profiles.EventManager')),
            ],
        ),
    ]
