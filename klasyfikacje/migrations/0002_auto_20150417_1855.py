# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klasyfikacje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbolpkwiu',
            name='dzieci',
            field=models.ManyToManyField(to='klasyfikacje.SymbolPKWIU', related_name='dzieci_rel_+', blank=True),
        ),
    ]
