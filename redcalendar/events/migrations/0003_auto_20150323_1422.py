# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150319_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='from_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_place',
            new_name='place',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_poster',
        ),
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(default=datetime.datetime(2015, 3, 23, 12, 21, 57, 822439, tzinfo=utc), upload_to=b'posters'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='to_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 12, 22, 4, 310923, tzinfo=utc), verbose_name=b'date'),
            preserve_default=False,
        ),
    ]
