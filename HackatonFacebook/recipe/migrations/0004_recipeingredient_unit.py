# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20150516_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='unit',
            field=models.ForeignKey(blank=True, to='recipe.Unit', null=True),
        ),
    ]
