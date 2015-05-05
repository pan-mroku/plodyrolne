# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NazwaGrupowania',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nazwa', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SymbolPKWIU',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('symbol', models.TextField(unique=True)),
                ('dzieci', models.ManyToManyField(to='klasyfikacje.SymbolPKWIU', blank=True)),
                ('nazwa', models.ForeignKey(to='klasyfikacje.NazwaGrupowania')),
            ],
            options={
                'ordering': ['symbol'],
            },
        ),
    ]
