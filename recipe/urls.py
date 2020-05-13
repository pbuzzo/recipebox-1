from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipeadd/', views.recipeadd),
    path('authoradd/', views.signup),
    path('recipe/<int:id>/', views.recipe),
    path('author/<int:id>/', views.author),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('signup/', views.signup)
]
