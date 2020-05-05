from django import forms
from recipe.models import Author


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=40)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.TextArea)
    time_required = forms.CharField(max_length=30, default='')
    instructions = forms.CharField(widget=forms.TextArea)


'''
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(default='')

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=30, default='')
    instructions = models.TextField()

    def __str__(self):
        return self.title
'''
