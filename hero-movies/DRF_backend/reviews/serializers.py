from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)
        read_only_fields = ('username',)


class ReviewListSerializer(serializers.ModelSerializer):

    class MovieTitleSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title', 'id', )

    reviewed_movie = MovieTitleSerializer(read_only=True)
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = Review
        exclude = ('content', )


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'user', 'reviewed_movie', 'title', 'content',)
        read_only_fields = ('reviewed_movie',)


class ReviewCommentSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ReviewComment
        fields = '__all__'
        read_only_fields = ('user', 'review', 'like_users', )


class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    user = UsernameSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    movie_detail = MovieSerializer(read_only=True)
    comments = ReviewCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'like_users', )
