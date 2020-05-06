from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index),
    path('recipeadd/', views.recipeadd),
    path('recipe/<int:id>/', views.recipe),
    path('author/<int:id>/', views.author)
]
