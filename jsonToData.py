# -*- coding: utf-8 -*-
import os
import sys

BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    "HackatonFacebook"
)
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = "HackatonFacebook.settings"
import json
import django
django.setup()
from HackatonFacebook.recipe.models import Recipe, Ingredient, RecipeIngredient


with open('recipes.json') as data_file:
    data = json.load(data_file)

for d in data:
    recipe = Recipe()
    if len(d['name']) >= 200:
        recipe.name = d['name'][:199]
    else:
        recipe.name = d['name']
    recipe.prepare_time = d['prep_time']
    recipe.income = d['portions']
    recipe.photo = d['picture_url']
    recipe.preparation = '\n'.join(d['instructions'])
    recipe.save()
    for ing in d['ingredients']:
        if len(ing) >= 200:
            ingredient = Ingredient(name=ing[:199])
        else:
            ingredient = Ingredient(name=ing)
        ingredient.save()
        recipe_ingredient = RecipeIngredient()
        recipe_ingredient.recipe = recipe
        recipe_ingredient.ingredient = ingredient
        recipe_ingredient.save()
