from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from recipe.models import RecipeItem, Author
from recipe.forms import RecipeAddForm, AuthorAddForm, LoginForm, SignUpForm


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def index(request):
    data = RecipeItem.objects.all()
    authors = Author.objects.all()
    recipes = RecipeItem.objects.all()
    if request.user.is_authenticated:
        current_author = Author.objects.get(name=request.user)
        favs = [
            item for item in recipes if item in current_author.favorites.all()
        ]
        return render(request, 'index.html', {'data': data, "favorites": favs})
    return render(request, 'index.html', {'data': data})


def recipe(request, id):
    data = RecipeItem.objects.get(id=id)
    return render(request, 'recipe.html', {'data': data})


@login_required
def recipeadd(request):
    html = 'generic_form.html'

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



def recipe_edit(request, id):
    html = "generic_form.html"
    recipe = RecipeItem.objects.get(id=id)
    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.description = data['description']
            recipe.author = data['author']
            recipe.time_required = data['time_required']
            recipe.instructions = data['instructions']
            recipe.save()
            return HttpResponseRedirect(reverse('recipe', args=(id,)))

    form = RecipeAddForm(initial={
        'title': recipe.title,
        'description': recipe.description,
        'author': recipe.author,
        'time_required': recipe.time_required,
        'instructions': recipe.instructions,
    })
    return render(request, html, {'form': form})



def author(request, id):
    person = Author.objects.get(id=id)
    recipes = RecipeItem.objects.filter(author=person)
    return render(request, 'author.html',
                  {'author': person, 'recipes': recipes})


@login_required
def authoradd(request):
    if request.user.is_staff:
        html = 'generic_form.html'
        if request.method == 'POST':
            form = AuthorAddForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(
                    username=data['username'],
                    password=data['password']
                )
                Author.objects.create(
                    user=user,
                    name=data['name'],
                    bio=data['bio']
                )
                return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()
    return render(request, html, {'form': form})


@login_required
def follow(request, id):
    if request.user.is_authenticated:
        recipe = RecipeItem.objects.get(id=id)
        follower = Author.objects.get(name=request.user)
        follower.favorites.add(recipe)
        follower.save()

    return HttpResponseRedirect(reverse('homepage'))


@login_required
def unfollow(request, id):
    if request.user.is_authenticated:
        recipe = RecipeItem.objects.get(id=id)
        follower = Author.objects.get(name=request.user)
        follower.favorites.remove(recipe)
        follower.save()

    return HttpResponseRedirect(reverse('homepage'))



def signup(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            Author.objects.create(
                user=user,
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = SignUpForm()
    return render(request, html, {'form': form})
