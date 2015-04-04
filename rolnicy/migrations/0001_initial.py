# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rolnik',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Imie', models.CharField(max_length=20)),
                ('Nazwisko', models.CharField(max_length=50)),
                ('Adres', models.CharField(max_length=100)),
            ],
        ),
    ]
