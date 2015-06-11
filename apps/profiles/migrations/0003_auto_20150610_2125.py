# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20150610_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('reg_datetime', models.DateTimeField(auto_now_add=True)),
                ('is_banned', models.BooleanField(default=False)),
                ('activity_index', models.FloatField(default=0.0)),
                ('city', models.ForeignKey(to='profiles.City')),
                ('user', models.OneToOneField(related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('reg_datetime', models.DateTimeField(auto_now_add=True)),
                ('is_banned', models.BooleanField(default=False)),
                ('legal_status', models.CharField(max_length=10, choices=[(b'LEGAL', b'Legal person'), (b'INDIVIDUAL', b'Individual person')])),
                ('activity_index', models.FloatField(default=0.0)),
                ('cities', models.ManyToManyField(to='profiles.City')),
                ('user', models.OneToOneField(related_name='eventmanager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='cities',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
