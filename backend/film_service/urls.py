from django.urls import path

from .views import (
    actor_detail,
    actor_list,
    category_detail,
    category_list,
    film_detail,
    film_list,
    genre_detail,
    genre_list,
    userfilms_detail,
    userfilms_list,
)

urlpatterns = [
    path("films/", film_list),
    path("films/<int:pk>/", film_detail),
    path("actors/", actor_list),
    path("actors/<int:pk>/", actor_detail),
    path("genres/", genre_list),
    path("genres/<int:pk>/", genre_detail),
    path("categories/", category_list),
    path("categories/<int:pk>/", category_detail),
    path("userfilms/", userfilms_list),
    path("userfilms/<int:pk>/", userfilms_detail),
]