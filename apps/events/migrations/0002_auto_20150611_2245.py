# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.ForeignKey(to='profiles.City'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_views',
            field=models.ManyToManyField(related_name='order_views_set', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(related_name='order_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='auctionorder',
            name='city',
            field=models.ForeignKey(to='profiles.City'),
        ),
        migrations.AddField(
            model_name='auctionorder',
            name='order_views',
            field=models.ManyToManyField(related_name='auctionorder_views_set', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='auctionorder',
            name='owner',
            field=models.ForeignKey(related_name='auctionorder_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
