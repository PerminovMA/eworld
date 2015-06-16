# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eworld', '0004_auto_20150615_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='video',
            field=models.TextField(help_text=b'iFrame', null=True, blank=True),
        ),
    ]
