from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index),
    path('recipe/', views.recipe),
    path('author/<int:id>/', views.author)
]
