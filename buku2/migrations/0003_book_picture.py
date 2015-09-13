# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('buku2', '0002_auto_20150829_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(default=datetime.date(2015, 9, 1), upload_to=b'profile_images', blank=True),
            preserve_default=False,
        ),
    ]
