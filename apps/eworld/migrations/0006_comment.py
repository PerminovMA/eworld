# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eworld', '0005_auto_20150615_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.CharField(max_length=10)),
                ('answer_to', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='eworld.Comment', null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
