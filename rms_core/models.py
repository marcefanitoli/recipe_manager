from django.db import models

class Recipe(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.RESTRICT, null=True, blank=True)
    start_date = models.DateTimeField('date started', null=True, blank=True)
    status = models.CharField(max_length=200, default="todo", blank=True)
    points = models.IntegerField()
    def __str__(self):
        return self.name


class RecipeInstance(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default="todo", blank=True)
    order = models.IntegerField()
    def __str__(self):
        return self.name

class Ingredients:
    pass

class Pantry:
     pass

class Supplies:
    pass
