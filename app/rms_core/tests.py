
from django.test import TestCase
from django.urls import reverse

from .models import Ingredient
from .forms import IngredientForm


class EnterIngredientTests(TestCase):

    def test_ingredient_added(self):
        """
        adds ingredient
        """
        data = {'name': "flour", 'description': "white", 'category': "carb", 'calorie_density': "10"}
        form = IngredientForm(data=data)
        self.assertTrue(form.is_valid())

        self.client.post(reverse('rms_core:ingredient_list'), data)