# -*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404
from .models import RecipeIngredient, Recipe, Ingredient


def MyFn(s):
    return -(s.values()[0]['count_have'] - s.values()[0]['count_no_have'])


class IngredientForm(forms.Form):
    ingredient = forms.CharField(max_length=200, required=False)


IngredientFormSet = formset_factory(IngredientForm)


class RecipeSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.ingredients = kwargs.pop('ingredients')
        super(RecipeSearchForm, self).__init__(*args, **kwargs)

    def get_queryset(self):
        ingredients = self.ingredients
        q = Q()
        # All RecipesIngredients filtered by user input
        for ingredient in ingredients:
            if ingredient:
                q = q | Q(ingredient__name__icontains=ingredient)
        recipe_ingredients = RecipeIngredient.objects.filter(q)

        # Recipes, search, no-repeat, sort
        recipes = {}
        for ri in recipe_ingredients:
            recipe_id = ri.recipe.id
            if recipe_id in recipes:
                recipes[recipe_id]['count_have'] += 1
                recipes[recipe_id]['count_no_have'] -= 1
                recipes[recipe_id]['ingredients_in'].append(ri.ingredient.name)
                recipes[recipe_id]['ingredients_out'].remove(ri.ingredient.name)
            else:
                recipe_obj = get_object_or_404(Recipe, pk=recipe_id)
                recipes[recipe_id] = {}
                recipes[recipe_id]['id'] = ri.recipe.id
                recipes[recipe_id]['name'] = ri.recipe.name
                recipes[recipe_id]['photo'] = ri.recipe.photo if ri.recipe.photo is not None else 'static/images/default.jpg'
                recipes[recipe_id]['preparation'] = ri.recipe.preparation.split('\n')
                recipes[recipe_id]['prepare_time'] = ri.recipe.prepare_time
                recipes[recipe_id]['income'] = ri.recipe.income
                recipes[recipe_id]['count_have'] = 1
                recipes[recipe_id]['count_no_have'] = recipe_obj.recipeingredient_set.count() - 1
                recipes[recipe_id]['likes'] = recipe_obj.like_set.count()
                recipes[recipe_id]['favorites'] = recipe_obj.favorite_set.count()
                recipes[recipe_id]['ingredients_in'] = []
                recipes[recipe_id]['ingredients_in'].append(ri.ingredient.name)
                recipes[recipe_id]['ingredients_out'] = []

                for recipe_ingredient in recipe_obj.recipeingredient_set.all().values_list('ingredient__name'):
                    recipes[recipe_id]['ingredients_out'].append(recipe_ingredient[0])

                recipes[recipe_id]['ingredients_out'].remove(ri.ingredient.name)
        # recipes = OrderedDict(sorted(recipes.items(), key=lambda t: (-(t[1]['count_have'] - t[1]['count_no_have']))))
        ret = []
        for key, value in recipes.items():
            ret.append({key: value})
        ret = sorted(ret, key=MyFn)
        return ret


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['user_add', 'description', 'photo']


class IngredientBaseForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = []

IngredientBaseFormSet = inlineformset_factory(Recipe, RecipeIngredient, exclude=[], form=IngredientBaseForm)
