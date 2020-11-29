from django import forms

class IngredientForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    description = forms.CharField(label='description', max_length=100)
    category = forms.CharField(label='category', max_length=100)
    calorie_density = forms.CharField(label='calorie_density', max_length=100)