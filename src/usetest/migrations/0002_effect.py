# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usetest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='effect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a', models.DecimalField(max_digits=3, decimal_places=0)),
                ('b', models.DecimalField(max_digits=3, decimal_places=0)),
                ('c', models.DecimalField(max_digits=3, decimal_places=0)),
                ('d', models.DecimalField(max_digits=3, decimal_places=0)),
                ('e', models.DecimalField(max_digits=3, decimal_places=0)),
            ],
        ),
    ]
