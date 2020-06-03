from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(
        'RecipeItem',
        blank=True,
        related_name='favorites',
        symmetrical=False  # follow does not go both ways, leave false
    )

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
