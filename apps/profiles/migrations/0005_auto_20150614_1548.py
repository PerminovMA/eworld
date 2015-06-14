# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_portfolio_portfolioimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='activity_index',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='eventmanager',
            name='activity_index',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
        ),
    ]
