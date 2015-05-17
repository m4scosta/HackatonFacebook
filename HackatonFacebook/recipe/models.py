# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    name = models.CharField(u'Nome', max_length=200)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(u'Nome', max_length=200)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    user_add = models.ForeignKey(User, null=True, blank=True, verbose_name=u'Usuário que adicionou')
    date_add = models.DateField(u'Data de cadastro', auto_now_add=True)
    name = models.CharField(u'Nome', max_length=200)
    photo = models.URLField(u'Foto', max_length=200, null=True, blank=True)
    photo_input = models.ImageField(u'Foto', upload_to='recipe/images/', null=True, blank=True)
    description = models.TextField(u'Descrição', null=True, blank=True)
    preparation = models.TextField(u'Preparo', null=True, blank=True)
    prepare_time = models.CharField(u'Tempo de preparo', max_length=100, null=True, blank=True)
    income = models.CharField(u'Rendimento', max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_ingredients(self):
        recipe_ingredients = self.recipeingredient_set.all().values_list('ingredient')
        qs = Ingredient.objects.filter(id__in=recipe_ingredients)
        return qs


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(u'Quantidade', max_length=100, null=True, blank=True)
    unit = models.ForeignKey(Unit, null=True, blank=True)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)


class Like(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
