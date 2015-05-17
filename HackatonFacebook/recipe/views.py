import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import RecipeSearchForm, IngredientForm, RecipeForm, IngredientBaseFormSet
from .models import Recipe, Like, Favorite


def home(request):
    return render(request, 'recipe/home.html', {})


@csrf_exempt
def recipes_list(request):
    context = {}
    if request.method == "POST":
        form_recipe = RecipeSearchForm(ingredients=json.loads(request.read())['ingredients'])
        qs = form_recipe.get_queryset()
        context['qs'] = json.dumps(qs)
        return HttpResponse(context['qs'], content_type="application/json")
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


def recipe_create_update(request, pk=None):
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk)
    else:
        recipe = None
    form = RecipeForm(request.POST or None, request.FILES, instance=recipe)
    formset = IngredientBaseFormSet(request.POST or None)
    context = {}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    context['form'] = form
    context['formset'] = formset
    return render(request, 'recipe/recipe_form.html', context)


@csrf_exempt
def like(request):
    if request.method == "POST":
        pk = json.loads(request.read())['recipe_id']
        recipe = get_object_or_404(Recipe, pk=pk)
        user = request.user
        user = get_object_or_404(User, id=user.pk)
        like = Like(recipe=recipe, user=user)
        like.save()
        return HttpResponse(json.dumps({'ok': 'ok'}))
    return HttpResponse(json.dumps({'false': 'false'}))


@csrf_exempt
def favoritos(request):
    if request.method == "POST":
        pk = json.loads(request.read())['recipe_id']
        recipe = get_object_or_404(Recipe, pk=pk)
        user = request.user
        user = get_object_or_404(User, id=user.pk)
        favorite = Favorite(recipe=recipe, user=user)
        favorite.save()
        return HttpResponse(json.dumps({'ok': 'ok'}))
    return HttpResponse(json.dumps({'false': 'false'}))
