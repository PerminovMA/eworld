# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20150923_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='amount',
            field=models.DecimalField(max_digits=11, decimal_places=2),
        ),
    ]
