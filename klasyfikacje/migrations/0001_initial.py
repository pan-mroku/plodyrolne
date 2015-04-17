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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nazwa', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StawkaVAT',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('wartosc', models.TextField()),
                ('nazwa', models.ManyToManyField(to='klasyfikacje.NazwaGrupowania')),
            ],
        ),
        migrations.CreateModel(
            name='SymbolPKWIU',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('symbol', models.TextField()),
                ('dzieci', models.ManyToManyField(related_name='dzieci_rel_+', to='klasyfikacje.SymbolPKWIU')),
                ('nazwa', models.OneToOneField(to='klasyfikacje.NazwaGrupowania')),
            ],
        ),
        migrations.AddField(
            model_name='stawkavat',
            name='symbol',
            field=models.ManyToManyField(to='klasyfikacje.SymbolPKWIU'),
        ),
    ]
