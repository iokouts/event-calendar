# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateTimeField(verbose_name=b'date')),
                ('event_place', models.CharField(max_length=100)),
                ('event_poster', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'./posters'), upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
