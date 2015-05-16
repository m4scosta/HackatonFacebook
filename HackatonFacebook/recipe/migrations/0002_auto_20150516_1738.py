# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='income',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'recipe/images', blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prepare_time',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
