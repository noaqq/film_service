from typing import Set

from django.db import models
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["username"]

    def __str__(self):
        return self.username
    
    def get_parametrs(self):
        return str(self.username), str(self.password), str(self.email)

class UserFilms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey("Film", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
    time_watched = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + " " + self.film.title
    
    def get_parametrs(self):
        return str(self.user), str(self.film), str(self.rating), str(self.favorite), str(self.time_watched)
    
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
    
    def get_parametrs(self):
        return str(self.title), str(self.description), str(self.country), str(self.year), str(self.director), str(self.rating), str(self.actors), str(self.genres), str(self.categories)
    
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
    
    def get_parametrs(self):
        return str(self.name), str(self.age), str(self.films)
    
    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        ordering = ["name"]

class Genre(models.Model):
    name = models.CharField(max_length=50)
    films = models.ManyToManyField(Film, related_name="Genres")

    def __str__(self):
        return self.name
    
    def get_parametrs(self):
        return str(self.name), str(self.films)
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ["name"]

class Category(models.Model):
    name = models.CharField(max_length=50)
    films = models.ManyToManyField(Film, related_name="Categories")

    def __str__(self):
        return self.name
    
    def get_parametrs(self):
        return str(self.name), str(self.films)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]