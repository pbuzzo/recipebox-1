from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index),
    path('recipe/<int:id>/', views.recipe),
    path('author/<int:id>/', views.author)
]
