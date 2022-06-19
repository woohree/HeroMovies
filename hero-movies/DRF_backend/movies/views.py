from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 영화추천 알고리즘
@api_view(['GET'])
def movie_recommendation(request):
    user = request.user
    fav_movies = user.fav_movies.all()
    voted_movies = Movie.objects.filter(id__in=request.user.voted_movies.values_list('movie'))
    wished_movies = Movie.objects.filter(id__in=request.user.wished_movies.all())
    user_keywords = {}
    queried_movies = []

    # 유저 선호 영화
    for fav_movie in fav_movies:
        for keyword_id in fav_movie.keywords.values_list('id'):
            if keyword_id[0] not in user_keywords:
                user_keywords.update({keyword_id[0]: 1})
            else:
                user_keywords[keyword_id[0]] += 1

    # 유저가 평점을 준 영화
    for voted_movie in voted_movies:
        score = voted_movie.votes.values_list('score')[0][0]
        # 평점에 가중치 적용
        weighted_score = (score - 5) / 2
        for keyword_id in voted_movie.keywords.values_list('id'):
            if keyword_id[0] not in user_keywords:
                user_keywords.update({keyword_id[0]: weighted_score})
            else:
                user_keywords[keyword_id[0]] += weighted_score

    # 유저가 찜해놓은 영화
    for wished_movie in wished_movies:
        for keyword_id in wished_movie.keywords.values_list('id'):
            if keyword_id[0] not in user_keywords:
                user_keywords.update({keyword_id[0]: 1})
            else:
                user_keywords[keyword_id[0]] += 1

    # 점수가 매겨진 키워드들을 내림차순 정렬
    sorted_keyword_ids = sorted(user_keywords, key=user_keywords.get, reverse=True)
    for sorted_keyword_id in sorted_keyword_ids:
        keyword = get_object_or_404(Keyword, id=sorted_keyword_id)
        # 조건 : 평정 7 이상, 평점 준 사람 1000 명 이상, 본 적 없음, 개봉됨, 평점 내림차순 정렬
        keyworded_movies = keyword.movies.filter(vote_average__gt=7, vote_count__gt=1000).exclude(id__in=voted_movies).order_by('-vote_average')[:6]
        queried_movies.extend(keyworded_movies)
    
    queried_movies = list(dict.fromkeys(queried_movies))
    # 정렬된 영화 객체 리스트를 콘푸로스트라이즈
    serializer = MovieListSerializer(queried_movies, many=True)
    return Response(serializer.data)


# 위시리스트 제공
@api_view(['GET'])
def wished_movie_list(request):
    wished_movies = Movie.objects.filter(id__in=request.user.wished_movies.all())
    serializer = MovieListSerializer(wished_movies, many=True)
    return Response(serializer.data)


# 평점 준 영화 목록 제공
@api_view(['GET'])
def voted_movie_list(request):
    voted_movies = Movie.objects.filter(id__in=request.user.voted_movies.values_list('movie'))
    serializer = MovieListSerializer(voted_movies, many=True)
    return Response(serializer.data)


# 영화 상세 정보
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 평점
@api_view(['POST', 'PUT', 'DELETE'])
def create_or_update_or_delete_vote(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    def create_vote():
        if request.user not in movie.voted_users.all():
            serializer = VoteSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie, user=request.user)
                # 평점 평균 계산식
                total_score = movie.vote_average * movie.vote_count + int(request.data.get('score'))
                movie.vote_count += 1
                movie.vote_average = total_score / movie.vote_count
                movie.save()
                serializer = MovieSerializer(movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # data = {"create_vote": f"{request.user} already voted on movie {movie.id}"}
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
    
    def update_vote():
        if request.user in movie.voted_users.all():
            vote = Vote.objects.get(user=request.user, movie=movie)
            serializer = VoteSerializer(instance=vote, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # 평점 평균 계산식
                total_score = movie.vote_average * movie.vote_count - vote.score + int(request.data.get('score'))
                movie.vote_average = total_score / movie.vote_count
                movie.save()
                serializer = MovieSerializer(movie)
                return Response(serializer.data)
        else:
            # data = {"update_vote": f"{request.user} not yet voted on movie {movie.id}"}
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
    
    def delete_vote():
        if request.user in movie.voted_users.all():
            vote = Vote.objects.get(user=request.user, movie=movie)
            total_score = movie.vote_average * movie.vote_count - vote.score
            movie.vote_count -= 1
            movie.vote_average = total_score / movie.vote_count
            movie.save()
            vote.delete()
            # data = {"delete_vote": f"{request.user} deleted voted on movie {movie.id}"}
            
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            # data = {"delete_vote": f"{request.user} not yet voted on movie {movie.id}"}
        
            serializer = MovieSerializer(movie)
            return Response(serializer.data)

    if request.method == 'POST':
        return create_vote()
    elif request.method == 'PUT':
        return update_vote()
    elif request.method == 'DELETE':
        return delete_vote()


# 영화 찜하기 또는 취소
@api_view(['PUT'])
def add_or_cancel_wish(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    def add_wish():
        movie.wishing_users.add(request.user)
        movie.save()
        # data = {
        #     "add_wish": f'{request.user} added movie<{movie.id}> on the wishlist'
        # }
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def cancel_wish():
        movie.wishing_users.remove(request.user)
        movie.save()
        # data = {
        #     "cancel_wish": f'{request.user} removed movie<{movie.id}> from the wishlist'
        # }
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    if request.user not in movie.wishing_users.all():
        return add_wish()
    else:
        return cancel_wish()


#   해당 영화에 달린 리뷰 조회 및 생성
from reviews.serializers import ReviewListSerializer, ReviewCreateSerializer
from reviews.models import Review
@api_view(['GET', 'POST'])
def movie_review_list_or_create(request, movie_id):
    def movie_review_list():
        movie_reviews = Review.objects.filter(reviewed_movie=movie_id)
        serializer = ReviewListSerializer(movie_reviews, many=True)
        return Response(serializer.data)

    def movie_review_create():
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(reviewed_movie=movie)
            
            reviews = Review.objects.filter(reviewed_movie=movie_id)
            serializer = ReviewListSerializer(reviews, many=True)
            return Response(serializer.data)

    if request.method == 'GET':
        return movie_review_list()
    elif request.method == 'POST':
        return movie_review_create()



# tmdb 데이터 수집 및 저장까지
import requests
@api_view(['POST'])
def import_from_tmdb(request):
    #   하이퍼 파라미터
    BASE_URL = 'https://api.themoviedb.org/3'
    api_key = '4674aa6ddbfec82653a5112fd7f0ee7c'
    language = 'ko-KR'
    #               mcu     dceu    superhero   ssu 삭제당함 ㅠㅠ    hero
    keyword_list = [180547, 229266, 9715]       # 296915            1701

    params = {
       'api_key': api_key,
       'language': language,
    }

    #   키워드에 해당하는 영화들의 아이디를 전부 받아온다.
    movie_ids = []

    for keyword in keyword_list:
        keyword_path = f'/keyword/{keyword}/movies'

        total_pages = requests.get(BASE_URL + keyword_path, params = params).json().get('total_pages')
        # print(total_pages)
        for page in range(1, total_pages+1):
            page_params = {
                'api_key': api_key,
                'language': language,
                'page': page,
            }
            movie_list = requests.get(BASE_URL + keyword_path, params = page_params).json().get('results')
            for movie in movie_list:
                movie_id = movie.get('id')
                movie_ids.append(movie_id)

    for movie_id in movie_ids:
        movie_detail_path = f'/movie/{movie_id}'
        movie_detail = requests.get(BASE_URL + movie_detail_path, params = params).json()

        if not Movie.objects.filter(pk=movie_id).exists():
            movie_serializer = MovieSerializer(data=movie_detail)
            # tmdb에서 가끔 거지같은 데이터를 제공하기 때문에 예외 발생시 그냥 스킵할 수 있게 한다.
            # 아니 왜 지네 발리데이션을 지네가 안지켜 진짜
            if movie_serializer.is_valid(raise_exception=False):
                movie_serializer.save()
            else:
                continue

        for genre in movie_detail.get('genres'):
            if not Genre.objects.filter(pk=genre.get('id')).exists():
                serializer = GenreSerializer(data=genre)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
        
        for production_company in movie_detail.get('production_companies'):
            if not ProductionCompany.objects.filter(pk=production_company.get('id')).exists():
                serializer = ProductionCompanySerializer(data=production_company)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

        for production_country in movie_detail.get('production_countries'):
            if not ProductionCountry.objects.filter(iso_3166_1=production_country.get('iso_3166_1')).exists():
                serializer = ProductionCountrySerializer(data=production_country)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

        for spoken_language in movie_detail.get('spoken_languages'):
            if not SpokenLanguage.objects.filter(iso_639_1=spoken_language.get('iso_639_1')).exists():
                serializer = SpokenLanguageSerializer(data=spoken_language)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

        
        genres = list(map(lambda x: x.get('id'), movie_detail.get('genres')))
        production_companies = list(map(lambda x: x.get('id'), movie_detail.get('production_companies')))

        production_countries = map(lambda x: ProductionCountry.objects.get(iso_3166_1=x).id,
                                    map(lambda x: x.get('iso_3166_1'), movie_detail.get('production_countries')))
        spoken_languages = map(lambda x: SpokenLanguage.objects.get(iso_639_1=x).id,
                                map(lambda x: x.get('iso_639_1'), movie_detail.get('spoken_languages')))

        movie = get_object_or_404(Movie, pk=movie_id)
        movie_serializer = MovieSerializer(instance=movie, data=movie_detail)
        if movie_serializer.is_valid(raise_exception=True):
            movie_serializer.save(genres=genres, production_companies=production_companies, 
                                    production_countries=production_countries, spoken_languages=spoken_languages)

            
        movie_keywords_path = f'/movie/{movie_id}/keywords'
        movie_credits_path = f'/movie/{movie_id}/credits'

        movie_keywords = requests.get(BASE_URL + movie_keywords_path, params = params).json().get('keywords')
        movie_casts = requests.get(BASE_URL + movie_credits_path, params = params).json().get('cast')
        
        for movie_keyword in movie_keywords:
            if not Keyword.objects.filter(pk=movie_keyword.get('id')).exists():
                # movie = get_object_or_404(Movie, pk=movie_id)
                serializer = KeywordSerializer(data=movie_keyword)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
            keyword = get_object_or_404(Keyword, pk=movie_keyword.get('id'))
            keyword.movies.add(movie)

        for movie_cast in movie_casts:
            if not Actor.objects.filter(pk=movie_cast.get('id')).exists():
                # movie = get_object_or_404(Movie, pk=movie_id)
                serializer = ActorSerializer(data=movie_cast)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
            actor = get_object_or_404(Actor, pk=movie_cast.get('id'))
            actor.movies.add(movie)

    return Response(status=status.HTTP_201_CREATED)
