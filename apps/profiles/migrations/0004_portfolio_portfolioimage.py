# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150613_1505'),
        ('profiles', '0003_auto_20150614_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='events.Category', blank=True)),
                ('event_manager', models.ForeignKey(to='profiles.EventManager')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=profiles.models.get_upload_image_path)),
                ('portfolio', models.ForeignKey(to='profiles.Portfolio')),
            ],
        ),
    ]
