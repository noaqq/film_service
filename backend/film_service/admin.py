from django.contrib import admin

from .models import Actor, Category, Film, Genre, UserFilms

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(UserFilms)
