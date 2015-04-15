# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rolnicy', '0002_auto_20150413_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rolnik',
            name='użytkownik',
        ),
        migrations.AddField(
            model_name='rolnik',
            name='Imie',
            field=models.CharField(max_length=20, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rolnik',
            name='Nazwisko',
            field=models.CharField(max_length=50, default=1),
            preserve_default=False,
        ),
    ]
