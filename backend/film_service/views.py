from drf_yasg.utils import swagger_auto_schema
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


@swagger_auto_schema(method="get", responses={200: UserSerializer(many=True)})
@api_view(["GET"])
def user_list(request):
    """
    List all users.
    """
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="post", request_body=UserSerializer, responses={200: UserSerializer}, parametrs=['username', 'password', 'email'])
@api_view(["POST"])
def user_create(request):
    """
    Create user.
    """
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="put", responses={200: UserSerializer}, parametrs=['username', 'password', 'email'])
@api_view(["PUT"])
def user_update(request, pk):
    """
    Update user.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="delete", responses={200: UserSerializer})
@api_view(["DELETE"])
def user_delete(request, pk):
    """
    Delete user.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="get", responses={200: UserFilmsSerializer(many=True)})
@api_view(["GET"])
def user_films_list(request):
    """
    List all user films.
    """
    if request.method == "GET":
        user_films = UserFilms.objects.all()
        serializer = UserFilmsSerializer(user_films, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="post", request_body=UserFilmsSerializer, responses={200: UserFilmsSerializer}, parametrs=['user', 'film', 'rating', 'favorite', 'time_watched'])
@api_view(["POST"])
def user_films_create(request):
    """
    Create user film.
    """
    if request.method == "POST":
        serializer = UserFilmsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="put", responses={200: UserFilmsSerializer}, parametrs=['user', 'film', 'rating', 'favorite', 'time_watched'])
@api_view(["PUT"])
def user_films_update(request, pk):
    """
    Update user film.
    """
    try:
        user_films = UserFilms.objects.get(pk=pk)
    except UserFilms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = UserFilmsSerializer(user_films, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="delete", responses={200: UserFilmsSerializer})
@api_view(["DELETE"])
def user_films_delete(request, pk):
    """
    Delete user film.
    """
    try:
        user_films = UserFilms.objects.get(pk=pk)
    except UserFilms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        user_films.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="get", responses={200: FilmSerializer(many=True)})
@api_view(["GET"])
def film_list(request):
    """
    List all films.
    """
    if request.method == "GET":
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="post", request_body=FilmSerializer, responses={200: FilmSerializer}, parametrs=['title', 'description', 'country', 'year', 'director', 'rating', 'actors', 'genres', 'categories'])
@api_view(["POST"])
def film_create(request):
    """
    Create film.
    """
    if request.method == "POST":
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="put", responses={200: FilmSerializer}, parametrs=['title', 'description', 'country', 'year', 'director', 'rating', 'actors', 'genres', 'categories'])
@api_view(["PUT"])
def film_update(request, pk):
    """
    Update film.
    """
    try:
        film = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="delete", responses={200: FilmSerializer})
@api_view(["DELETE"])
def film_delete(request, pk):
    """
    Delete film.
    """
    try:
        film = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="get", responses={200: ActorSerializer(many=True)})
@api_view(["GET"])
def actor_list(request):
    """
    List all actors.
    """
    if request.method == "GET":
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="post", request_body=ActorSerializer, responses={200: ActorSerializer}, parametrs=['name', 'surname', 'age', 'country'])
@api_view(["POST"])
def actor_create(request):
    """
    Create actor.
    """
    if request.method == "POST":
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="put", responses={200: ActorSerializer}, parametrs=['name', 'surname', 'age', 'country'])
@api_view(["PUT"])
def actor_update(request, pk):
    """
    Update actor.
    """
    try:
        actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="delete", responses={200: ActorSerializer})
@api_view(["DELETE"])
def actor_delete(request, pk):
    """
    Delete actor.
    """
    try:
        actor = Actor.objects.get(pk=pk)
    except Actor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="get", responses={200: GenreSerializer(many=True)})
@api_view(["GET"])
def genre_list(request):
    """
    List all genres.
    """
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="post", request_body=GenreSerializer, responses={200: GenreSerializer}, parametrs=['name'])
@api_view(["POST"])
def genre_create(request):
    """
    Create genre.
    """
    if request.method == "POST":
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="put", responses={200: GenreSerializer}, parametrs=['name'])
@api_view(["PUT"])
def genre_update(request, pk):
    """
    Update genre.
    """
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="delete", responses={200: GenreSerializer})
@api_view(["DELETE"])
def genre_delete(request, pk):
    """
    Delete genre.
    """
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="get", responses={200: CategorySerializer(many=True)})
@api_view(["GET"])
def category_list(request):
    """
    List all categories.
    """
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="post", request_body=CategorySerializer, responses={200: CategorySerializer}, parametrs=['name'])
@api_view(["POST"])
def category_create(request):
    """
    Create category.
    """
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="put", responses={200: CategorySerializer}, parametrs=['name'])
@api_view(["PUT"])
def category_update(request, pk):
    """
    Update category.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="delete", responses={200: CategorySerializer})
@api_view(["DELETE"])
def category_delete(request, pk):
    """
    Delete category.
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

