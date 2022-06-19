
from django.db import models
from django.conf import settings


class Movie(models.Model):
    # query로 movie id 리스트만 받아온 후, 개별 아이디에 대해 쿼리 넣어서 get details!
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200, null=True, blank=True)
    genres = models.ManyToManyField('Genre', related_name='genre_movies')
    id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=20)
    original_title = models.CharField(max_length=100)
    overview = models.CharField(null=True, blank=True, max_length=1000)
    popularity = models.FloatField()
    poster_path = models.CharField(null=True, blank=True, max_length=200)
    production_companies = models.ManyToManyField('ProductionCompany', related_name='production_movies')
    production_countries = models.ManyToManyField('ProductionCountry', related_name='production_movies')
    #               format date "yyyy-mm-dd"
    release_date = models.DateField()
    revenue = models.IntegerField()
    runtime = models.IntegerField(null=True, blank=True)
    spoken_languages = models.ManyToManyField('SpokenLanguage', related_name='movies')

    STATUS_CHOICES = [
        ('Rumored', 'Rumored'),
        ('Planned', 'Planned'),
        ('In Production', 'In Production'),
        ('Post Production', 'Post Production'),
        ('Released', 'Released'),
        ('Canceled', 'Canceled'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    tagline = models.CharField(null=True, blank=True, max_length=200)
    title = models.CharField(max_length=200)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    
    # local definition fields
    voted_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Vote', through_fields=('movie', 'user'), related_name='votes')
    # 찜한 유저들
    wishing_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wished_movies')
    # keywords = models.ManyToManyField('Keyword', on_delete=models.CASCADE, related_name='keyword_movies')
    # actors = models.ManyToManyField('Actor')

    class Meta:
        ordering = ['-release_date']


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    # genre_movies = models.ManyToManyField(Movie, on_delete=models.CASCADE, related_name='movie_genres')


class ProductionCompany(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    logo_path = models.CharField(null=True, blank=True, max_length=100)
    origin_country = models.CharField(null=True, blank=True, max_length=100)


class ProductionCountry(models.Model):
    iso_3166_1 = models.CharField(max_length=100)
    name = models.CharField(null=True, blank=True, max_length=100)


class SpokenLanguage(models.Model):
    iso_639_1 = models.CharField(max_length=20)
    name = models.CharField(null=True, blank=True, max_length=100)


class Vote(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='voted_movies')
    score = models.IntegerField() # null=True, blank=True


class Keyword(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    # Movies 수가 많기 때문에 Keyword로 검색 시 속도를 빠르게 하기 위해 이쪽에 정의한다.
    movies = models.ManyToManyField('Movie', related_name='keywords')


class Actor(models.Model):
    adult = models.BooleanField()
    gender = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    popularity = models.FloatField()
    profile_path = models.CharField(null=True, blank=True, max_length=100)
    character = models.CharField(null=True, blank=True, max_length=200)
    movies = models.ManyToManyField('Movie', related_name='actors')