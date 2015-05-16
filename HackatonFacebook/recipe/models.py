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
    user_add = models.ForeignKey(User)
    date_add = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='recipe/images', null=True, blank=True)
    description = models.TextField()
    preparation = models.TextField()
    prepare_time = models.CharField(max_length=100, null=True, blank=True)
    income = models.CharField(max_length=100, null=True, blank=True)  # rendimento

    def __unicode__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.DecimalField(decimal_places=4, max_digits=10)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)


class Like(models.Model):
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
