# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import eworld.models


class Migration(migrations.Migration):

    dependencies = [
        ('eworld', '0002_auto_20150613_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attach',
            name='file',
            field=models.FileField(upload_to=eworld.models.get_upload_file_path),
        ),
    ]
