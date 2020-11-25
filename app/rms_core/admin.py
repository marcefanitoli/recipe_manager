from django.contrib import admin
from .models import Ingredient, Supply, Pantry, Recipe, RecipeInstance

admin.site.register(Ingredient)
admin.site.register(Supply)
admin.site.register(Pantry)
admin.site.register(Recipe)
admin.site.register(RecipeInstance)