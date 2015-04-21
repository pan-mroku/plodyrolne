# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klasyfikacje', '0002_auto_20150417_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nazwagrupowania',
            name='nazwa',
            field=models.TextField(unique=True),
        ),
    ]
