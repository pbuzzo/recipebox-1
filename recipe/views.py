from django.shortcuts import render

from recipe.models import RecipeItem
# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})
