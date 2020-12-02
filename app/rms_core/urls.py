from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'rms_core'

urlpatterns = [
    path('', views.index, name='index'),
    path('ingredient/add/', views.ingredient_add, name='ingredient_add'),
    path('ingredient/', views.ingredient_list, name='ingredient_list'),
    path('ingredient/<int:ingredient_id>/', views.ingredient_detail, name='ingredient_detail'),
    path('supply/', views.supply_list, name='supply_list'),
    path('supply/<int:supply_id>/', views.supply_detail, name='supply_detail'),
    path('pantry/', views.pantry_list, name='pantry_list'),
    path('pantry/<int:pantry_id>/', views.pantry_detail, name='pantry_detail'),
    path('recipe/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe_instance/', views.recipe_instance_list, name='recipe_instance_list'),
    path('recipe_instance/<int:recipe_instance_id>/', views.recipe_instance_detail, name='recipe_instance_detail'),

]

urlpatterns += staticfiles_urlpatterns()
