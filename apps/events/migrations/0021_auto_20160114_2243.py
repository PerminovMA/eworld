# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0020_auto_20160114_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('answer_to', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='events.OrderComment', null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auctionorder',
            name='comments',
            field=models.ManyToManyField(to='events.OrderComment', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='comments',
            field=models.ManyToManyField(to='events.OrderComment', blank=True),
        ),
    ]
