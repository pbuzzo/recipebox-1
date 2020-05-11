from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipeadd/', views.recipeadd),
    path('authoradd/', views.authoradd),
    path('recipe/<int:id>/', views.recipe),
    path('author/<int:id>/', views.author),
    path('login/', views.loginview),
    path('signup/', views.signup)
]
