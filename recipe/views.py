from django.shortcuts import render

from recipe.models import RecipeItem, Author
from recipe.forms import RecipeAddForm
# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


def recipe(request):
    data = RecipeItem.objects.all()
    return render(request, 'recipe.html', {'data': data})


def recipeadd(request):
    html = 'recipeaddform.html'

    

    form = RecipeAddForm()

    return render(request, html, {'form': form})


def author(request, id):
    person = Author.objects.get(id=id)
    recipes = RecipeItem.objects.filter(author=person)
    return render(request, 'author.html',
                  {'author': person, 'recipes': recipes})
