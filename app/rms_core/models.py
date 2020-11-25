from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200, default="", blank=True)
    description = models.CharField(max_length=200, default="", blank=True)
    category = models.CharField(max_length=200, default="", blank=True)
    calorie_density = models.CharField(max_length=200, default="", blank=True)
    def __str__(self):
        return self.name


class Supply(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT, null=True, blank=True)
    price = models.CharField(max_length=200, default="", blank=True)
    servings_per_unit = models.IntegerField(blank=True)
    expiration_period  = models.IntegerField(blank=True)
    def __str__(self):
        return str(self.ingredient)


class Pantry(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.RESTRICT, null=True, blank=True)
    servings_remaining = models.IntegerField(blank=True)
    expiration_date = models.DateTimeField('date expires', null=True, blank=True)
    def __str__(self):
        return str(self.supply)


class Recipe(models.Model):
    ingredients = models.ManyToManyField(Ingredient)
    add_date = models.DateTimeField('date added', null=True, blank=True)
    instructions = models.CharField(max_length=200, default="", blank=True)
    name = models.CharField(max_length=200, default="", blank=True)
    serves = models.IntegerField()
    prep_time = models.IntegerField()
    calories = models.IntegerField()
    seasonality = models.CharField(max_length=200, default="", blank=True)
    rating = models.IntegerField()
    def __str__(self):
        return self.name


class RecipeInstance(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.RESTRICT)  # CASCADE
    made_date = models.DateTimeField('date made', null=True, blank=True)
    comments = models.CharField(max_length=200, default="", blank=True)
    changes = models.CharField(max_length=200, default="todo", blank=True)
    rating = models.IntegerField()
    def __str__(self):
        return str(self.recipe)