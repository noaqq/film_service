from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Actor, Category, Film, Genre, User, UserFilms
from .serializers import (
    ActorSerializer,
    CategorySerializer,
    FilmSerializer,
    GenreSerializer,
    UserFilmsSerializer,
    UserSerializer,
)


@api_view(["GET", "POST"])
def film_list(request):
    if request.method == "GET":
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(["GET", "PUT", "DELETE"])
def film_detail(request, pk):
    try:
        film = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FilmSerializer(film)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET", "POST"])
def actor_list(request):
    if request.method == "GET":
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(["GET", "PUT", "DELETE"])
def actor_detail(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET", "POST"])
def genre_list(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(["GET", "PUT", "DELETE"])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET", "POST"])
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET", "POST"])
def userfilms_list(request):
    if request.method == "GET":
        userfilms = UserFilms.objects.all()
        serializer = UserFilmsSerializer(userfilms, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserFilmsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(["GET", "PUT", "DELETE"])
def userfilms_detail(request, pk):
    try:
        userfilms = UserFilms.objects.get(pk=pk)
    except UserFilms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserFilmsSerializer(userfilms)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserFilmsSerializer(userfilms, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        userfilms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
