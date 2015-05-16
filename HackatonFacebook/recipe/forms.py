# -*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from django.forms.formsets import formset_factory
from .models import Unit, Ingredient, RecipeIngredient, Recipe


class IngredientForm(forms.Form):
    quantity = forms.CharField(required=False)
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(), required=False)
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(), required=False)


IngredientFormSet = formset_factory(IngredientForm)


class RecipeSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.ingredients = kwargs.pop('ingredients')
        super(RecipeSearchForm, self).__init__(*args, **kwargs)

    def get_queryset(self):
        ingredients = self.ingredients.getlist('ingredient')
        units = self.ingredients.getlist('unit')
        quantities = self.ingredients.getlist('quantity')
        q = Q()
        for a, b, c in zip(ingredients, units, quantities):
            print a, b, c
            if a:
                q = q | Q(recipe=a)
            if b:
                q = q | Q(ingredient=b)
        recipe_ingredients = RecipeIngredient.objects.filter(q)
        qs = Recipe.objects.filter(id__in=recipe_ingredients)
        return qs
