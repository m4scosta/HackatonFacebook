# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_auto_20150516_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo_input',
            field=models.ImageField(upload_to=b'recipe/images/', null=True, verbose_name='Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_add',
            field=models.DateField(auto_now_add=True, verbose_name='Data de cadastro'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True, verbose_name='Descri\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='income',
            field=models.CharField(max_length=100, null=True, verbose_name='Rendimento', blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.URLField(null=True, verbose_name='Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation',
            field=models.TextField(null=True, verbose_name='Preparo', blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepare_time',
            field=models.CharField(max_length=100, null=True, verbose_name='Tempo de preparo', blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='user_add',
            field=models.ForeignKey(verbose_name='Usu\xe1rio que adicionou', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(max_length=100, null=True, verbose_name='Quantidade', blank=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
    ]
