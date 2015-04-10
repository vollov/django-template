# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('kilometers', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=2000)),
                ('engine_size', models.DecimalField(default=0.0, max_digits=3, decimal_places=1)),
                ('drivetrain', models.CharField(default=b'FWD', max_length=3, choices=[(b'FWD', b'Front wheel drive (FWD)'), (b'AWD', b'All wheel drive (AWD)'), (b'RWD', b'Rear wheel drive (RWD)'), (b'OT', b'Other')])),
                ('transmition', models.CharField(default=b'AU', max_length=2, choices=[(b'AU', b'Automatic'), (b'MA', b'Manual'), (b'OT', b'Other')])),
                ('color', models.CharField(max_length=20)),
                ('interanl_color', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
