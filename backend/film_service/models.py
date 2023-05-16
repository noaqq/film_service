from django.db import models
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"]
class UserFilms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey("Film", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
    time_watched = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + " " + self.film.title
    
    class Meta:
        verbose_name = "UserFilm"
        verbose_name_plural = "UserFilms"
        ordering = ["user", "film"]

class Film(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="UNKNOWN")
    year = models.IntegerField()
    director = models.CharField(max_length=50)
    rating = models.IntegerField()
    actors = models.ManyToManyField("Actor", related_name="Films")
    genres = models.ManyToManyField("Genre", related_name="Films")
    categories = models.ManyToManyField("Category", related_name="Films")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"
        ordering = ["title"]

class Actor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    films = models.ManyToManyField(Film, related_name="Actors")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        ordering = ["name"]

class Genre(models.Model):
    name = models.CharField(max_length=50)
    films = models.ManyToManyField(Film, related_name="Genres")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ["name"]

class Category(models.Model):
    name = models.CharField(max_length=50)
    films = models.ManyToManyField(Film, related_name="Categories")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]