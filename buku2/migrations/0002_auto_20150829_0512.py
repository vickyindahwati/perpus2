# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buku2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengarang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='pengarang',
            field=models.ForeignKey(blank=True, to='buku2.Pengarang', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='sinopsis',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
