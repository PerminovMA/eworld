# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=13, choices=[(b'CLIENT', b'Client'), (b'EVENT_MANAGER', b'Event Manager')])),
                ('legal_status', models.CharField(blank=True, max_length=10, null=True, help_text=b'Required only for event managers.', choices=[(b'LEGAL', b'Legal person'), (b'INDIVIDUAL', b'Individual person')])),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('reg_datetime', models.DateTimeField(auto_now_add=True)),
                ('is_banned', models.BooleanField(default=False)),
                ('activity_index', models.FloatField(default=0.0)),
                ('cities', models.ManyToManyField(to='profiles.City', null=True, blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='EventManager',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='profiles.Country'),
        ),
    ]
