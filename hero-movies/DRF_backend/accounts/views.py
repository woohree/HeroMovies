from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


User = get_user_model()

@api_view(['GET', 'POST'])
def profile_detail_or_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    def profile_detail():
        serializer = ProfileSerializer(instance=user)
        return Response(serializer.data)

    def profile_update():
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)

    if request.method == 'GET':
        return profile_detail()
    elif request.method == 'POST':
        return profile_update()


# @api_view(['POST', 'PUT'])
# def fav_movies_list_or_create_or_update(request):
#     user_id = request.user.get('id')

#     def favs_list():
#         pass

#     def favs_create():

#     def favs_update():
#         pass
    
#     if request.method == 'GET':
#         return favs_list()
#     elif request.method == 'POST':
#         return favs_create()
#     elif request.method == 'PUT':
#         return favs_update()


# 선호 영화 고를 수 있게 보여주기 (9개)
COLLECTION = 9
from random import sample
@api_view(['GET'])
def fav_select_list(request):
    movie_ids = list(map(lambda x: x[0], Movie.objects.all().exclude(poster_path=None).values_list('id')))
    random_movie_ids = sample(movie_ids, COLLECTION)
    random_movies = Movie.objects.filter(id__in=random_movie_ids)
    serializer = FavSelectSerializer(random_movies, many=True)
    return Response(serializer.data)

# 위에서 선택한 영화 객체의 리스트를 받아서 User 에 저장
@api_view(['POST'])
def fav_create(request):
    user = request.user
    user.fav_movies.all().delete()

    for data in request.data:
        print(data.get('id'))
        movie = Movie.objects.filter(id=data.get('id'))
        print(movie)
        movie.fav_users.add(user)
        # user.fav_movies.add(data.get('id'))
    movie.save()
    # user.save()
    
    print(user.fav_movies.all())
    return Response(movie)