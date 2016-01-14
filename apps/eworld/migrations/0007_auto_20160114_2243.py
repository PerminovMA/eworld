# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eworld', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='answer_to',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
