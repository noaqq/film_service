# Generated by Django 4.1.2 on 2023-05-16 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=100)),
                ("year", models.IntegerField()),
                ("director", models.CharField(max_length=50)),
                ("rating", models.IntegerField()),
            ],
            options={
                "verbose_name": "Film",
                "verbose_name_plural": "Films",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "ordering": ["username"],
            },
        ),
        migrations.CreateModel(
            name="UserFilms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.IntegerField(default=0)),
                ("favorite", models.BooleanField(default=False)),
                ("time_watched", models.IntegerField(default=0)),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="film_service.film",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="film_service.user",
                    ),
                ),
            ],
            options={
                "verbose_name": "UserFilm",
                "verbose_name_plural": "UserFilms",
                "ordering": ["user", "film"],
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "films",
                    models.ManyToManyField(
                        related_name="Genres", to="film_service.film"
                    ),
                ),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "films",
                    models.ManyToManyField(
                        related_name="Categories", to="film_service.film"
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                (
                    "films",
                    models.ManyToManyField(
                        related_name="Actors", to="film_service.film"
                    ),
                ),
            ],
            options={
                "verbose_name": "Actor",
                "verbose_name_plural": "Actors",
                "ordering": ["name"],
            },
        ),
    ]