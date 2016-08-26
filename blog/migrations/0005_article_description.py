# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160820_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]
