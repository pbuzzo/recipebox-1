from django import forms
from recipe.models import Author


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=40)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=40)
    bio = forms.CharField(widget=forms.Textarea)
