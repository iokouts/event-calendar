# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_poster',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/posters'), upload_to=b''),
            preserve_default=True,
        ),
    ]
