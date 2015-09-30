# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, serialize=False, verbose_name='Activation key', primary_key=True)),
                ('name', models.CharField(max_length=16, null=True, blank=True)),
                ('email', models.EmailField(max_length=60, null=True, blank=True)),
                ('sin', models.CharField(max_length=24, null=True, blank=True)),
                ('address', models.CharField(max_length=125, null=True, blank=True)),
                ('phone', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
    ]
