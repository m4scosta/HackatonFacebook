from django.shortcuts import render, get_object_or_404
from .forms import RecipeSearchForm, IngredientForm
from .models import Recipe


def home(request):
    return render(request, 'recipe/home.html', {})


def test_home(request):
    form1 = IngredientForm(request.GET or None)
    form2 = IngredientForm(request.GET or None)
    context = {}
    context['form1'] = form1
    context['form2'] = form2
    if request.method == "GET" and request.GET:
        form_recipe = RecipeSearchForm(ingredients=request.GET)
        qs = form_recipe.get_queryset()
        context['qs'] = qs
        return render(request, 'recipe/test_list.html', context)
    return render(request, 'recipe/test_home.html', context)


def test_details(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {}
    context['recipe'] = recipe
    return render(request, 'recipe/test_details.html', context)
