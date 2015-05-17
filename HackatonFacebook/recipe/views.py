from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import RecipeSearchForm, IngredientForm
from .models import Recipe


def home(request):
    return render(request, 'recipe/home.html', {})


@csrf_exempt
def recipes_list(request):
    context = {}
    if request.method == "POST":
        form_recipe = RecipeSearchForm(ingredients=request.GET)
        qs = form_recipe.get_queryset()
        context['qs'] = qs
        return render(request, 'recipe/test_list.html', context)
    return render(request, 'recipe/test_home.html', context)


def test_home(request):
    form1 = IngredientForm(request.GET or None)
    form2 = IngredientForm(request.GET or None)
    form3 = IngredientForm(request.GET or None)
    form4 = IngredientForm(request.GET or None)
    context = {}
    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3
    context['form4'] = form4
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
