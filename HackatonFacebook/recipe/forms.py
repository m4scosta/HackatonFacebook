# -*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from django.forms.formsets import formset_factory
from .models import Ingredient, RecipeIngredient, Recipe


class IngredientForm(forms.Form):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(), required=False)


IngredientFormSet = formset_factory(IngredientForm)


class RecipeSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.ingredients = kwargs.pop('ingredients')
        super(RecipeSearchForm, self).__init__(*args, **kwargs)

    def get_queryset(self):
        ingredients = self.ingredients.getlist('ingredient')
        q = Q()
        for ingredient in ingredients:
            if ingredient:
                q = q | Q(ingredient=ingredient)
        recipe_ingredients = RecipeIngredient.objects.filter(q)
        qs = Recipe.objects.filter(id__in=recipe_ingredients)
        return qs
