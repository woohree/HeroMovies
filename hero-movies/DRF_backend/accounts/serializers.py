from os import set_inheritable
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from movies.models import Movie
from movies.serializers import MovieListSerializer, VoteSerializer
from reviews.serializers import ReviewListSerializer
from articles.serializers import ArticleListSerializer


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    )
    email = serializers.EmailField(required=False, help_text="optional")
    profile_image = serializers.ImageField(required=False, help_text="optional")
    introduction = serializers.CharField(required=False, help_text="optional. maximum 200 characters")
    class Meta:
        model = get_user_model()
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True, read_only=True)
    articles = ArticleListSerializer(many=True, read_only=True)
    votes = MovieListSerializer(many=True, read_only=True)
    wished_movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'
        excludes = ('password')
        read_only_fields = ('followings', 'fav_movies', )


class FavSelectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'poster_path', 'title')


class FavCreateSerializer(serializers.ModelSerializer):
    fav_movies = FavSelectSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'fav_movies')