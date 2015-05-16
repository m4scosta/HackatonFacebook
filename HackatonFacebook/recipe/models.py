from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    user_add = models.ForeignKey(User, null=True, blank=True)
    date_add = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    photo = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    preparation = models.TextField(null=True, blank=True)
    prepare_time = models.CharField(max_length=100, null=True, blank=True)
    income = models.CharField(max_length=100, null=True, blank=True)  # rendimento

    def __unicode__(self):
        return self.name

    def get_ingredients(self):
        recipe_ingredients = self.recipeingredient_set.all().values_list('ingredient')
        qs = Ingredient.objects.filter(id__in=recipe_ingredients)
        return qs


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    unit = models.ForeignKey(Unit, null=True, blank=True)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)


class Like(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
