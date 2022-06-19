from decimal import ROUND_HALF_UP
from unicodedata import decimal
from rest_framework import serializers
from .models import *


class MovieListSerializer(serializers.ModelSerializer):
    class KeywordListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Keyword
            fields = ('id', 'name', )
    class GenreListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)
    keywords = KeywordListSerializer(many=True, read_only=True)
    genres = GenreListSerializer(many=True, read_only=True)
    vote_average = serializers.DecimalField(max_digits=3, decimal_places=1, rounding=ROUND_HALF_UP)
    class Meta:
        model = Movie
        fields = ('id', 'poster_path', 'genres', 'release_date', 'runtime', 'title', 'tagline',
                    'status', 'vote_average', 'voted_users', 'wishing_users', 'keywords',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ProductionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCompany
        fields = '__all__'

class ProductionCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCountry
        fields = '__all__'

class SpokenLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpokenLanguage
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Keyword
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class KeywordListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Keyword
            fields = ('id', 'name', )
    
    class ActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('id', 'name', 'profile_path', 'character', )

    genres = GenreSerializer(many=True, read_only=True)
    production_companies = ProductionCompanySerializer(many=True, read_only=True)
    production_countries = ProductionCountrySerializer(many=True, read_only=True)
    spoken_languages = SpokenLanguageSerializer(many=True, read_only=True)

    keywords = KeywordListSerializer(many=True, read_only=True)
    actors = ActorListSerializer(many=True, read_only=True)
    vote_average = serializers.DecimalField(max_digits=3, decimal_places=1, rounding=ROUND_HALF_UP)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('voted_users', 'wishing_users', )


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


# class MovieCreateSerializer(serializers.ModelSerializer):

#     genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
#     production_companies = serializers.PrimaryKeyRelatedField(queryset=ProductionCompany.objects.all(), many=True)
#     production_countries = serializers.PrimaryKeyRelatedField(queryset= ProductionCountry.objects.all(), many=True)
#     spoken_languages = serializers.PrimaryKeyRelatedField(queryset= SpokenLanguage.objects.all(), many=True)

#     class Meta:
#         model = Movie
#         fields = '__all__'
#         read_only_fields = ('voted_users', 'wishing_users', )

#     def create(self, validated_data):
#         movie = Movie.objects.create(**validated_data)
#         for genre in validated_data["genres"]:
#             movie.genres.add(genre)
#         movie.save()
#         return movie

#     def update(self, instance, validated_data):
#         for item in validated_data:
#             if Movie._meta.get_field(item):
#                 setattr(instance, item, validated_data[item])
#         Genre.objects.filter(instance__in=Genre.genre_movies).delete()

#         for genre in validated_data["genres"]:
#             instance.genres.add(genre)
#         instance.save()
#         return instance

