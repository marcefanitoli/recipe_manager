from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Ingredient, Supply, Pantry, Recipe, RecipeInstance

def index(request):
    return render(request, 'rms_core/index.html')

def ingredient_list(request):
    generic_list = Ingredient.objects.order_by('-id')[:20]
    context = {'generic_list': generic_list}
    return render(request, 'rms_core/ingredient_list.html', context)

def supply_list(request):
    generic_list = Supply.objects.order_by('-id')[:20]
    context = {'generic_list': generic_list}
    return render(request, 'rms_core/supply_list.html', context)

def pantry_list(request):
    generic_list = Pantry.objects.order_by('-id')[:20]
    context = {'generic_list': generic_list}
    return render(request, 'rms_core/pantry_list.html', context)

def recipe_list(request):
    generic_list = Recipe.objects.order_by('-id')[:20]
    context = {'generic_list': generic_list}
    return render(request, 'rms_core/recipe_list.html', context)

def recipe_instance_list(request):
    generic_list = RecipeInstance.objects.order_by('-id')[:20]
    context = {'generic_list': generic_list}
    return render(request, 'rms_core/recipe_instance_list.html', context)

def ingredient_detail(request, ingredient_id):
    item = get_object_or_404(Ingredient, pk=ingredient_id)
    context = { 'item': item,}
    return render(request, 'rms_core/ingredient_detail.html', context)

def supply_detail(request, supply_id):
    item = get_object_or_404(Supply, pk=supply_id)
    context = { 'item': item,}
    return render(request, 'rms_core/supply_detail.html', context)

def pantry_detail(request, pantry_id):
    item = get_object_or_404(Pantry, pk=pantry_id)
    context = { 'item': item,}
    return render(request, 'rms_core/pantry_detail.html', context)

def recipe_detail(request, recipe_id):
    item = get_object_or_404(Recipe, pk=recipe_id)
    generic_list = item.ingredients_set.all().order_by('id')
    context = { 'item': item, 'generic_list': generic_list,}
    return render(request, 'rms_core/recipe_detail.html', context)

def recipe_instance_detail(request, recipe_instance_id):
    item = get_object_or_404(RecipeInstance, pk=recipe_instance_id)
    context = { 'item': item,}
    return render(request, 'rms_core/recipe_instance_detail.html', context)
