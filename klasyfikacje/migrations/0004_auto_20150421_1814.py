# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klasyfikacje', '0003_auto_20150421_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stawkavat',
            name='nazwa',
        ),
        migrations.RemoveField(
            model_name='stawkavat',
            name='symbol',
        ),
        migrations.AlterField(
            model_name='symbolpkwiu',
            name='nazwa',
            field=models.ForeignKey(to='klasyfikacje.NazwaGrupowania'),
        ),
        migrations.DeleteModel(
            name='StawkaVAT',
        ),
    ]
