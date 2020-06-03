from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipeadd/', views.recipeadd, name='recipe add'),
    path('recipe_edit/<int:id>/', views.recipe_edit, name="recipe edit"),
    path('follow/<int:id>/', views.follow, name="follow"),
    path('unfollow/<int:id>/', views.unfollow, name="unfollow"),
    path('authoradd/', views.authoradd, name='author add'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('author/<int:id>/', views.author, name='author'),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('signup/', views.signup)
]
