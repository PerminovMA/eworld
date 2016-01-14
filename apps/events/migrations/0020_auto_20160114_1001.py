# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20160114_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercomment',
            name='answer_to',
        ),
        migrations.RemoveField(
            model_name='ordercomment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='auctionorder',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='order',
            name='comments',
        ),
        migrations.DeleteModel(
            name='OrderComment',
        ),
    ]
