from django.shortcuts import render, reverse, HttpResponseRedirect

from recipe.models import RecipeItem, Author
from recipe.forms import RecipeAddForm, AuthorAddForm
# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


def recipe(request, id):
    data = RecipeItem.objects.get(id=id)
    return render(request, 'recipe.html', {'data': data})


def recipeadd(request):
    html = 'recipeaddform.html'

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeAddForm()

    return render(request, html, {'form': form})


def author(request, id):
    person = Author.objects.get(id=id)
    recipes = RecipeItem.objects.filter(author=person)
    return render(request, 'author.html',
                  {'author': person, 'recipes': recipes})


def authoradd(request):
    html = 'authoraddform.html'

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render(request, html, {'form': form})
