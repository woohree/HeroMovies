from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'id')
        read_only_fields = ('username', 'id')


# 게시판 메인 페이지
class ArticleListSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Article
        exclude = ('content',)


# 대댓글
class ArticleCommentCommentSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ArticleCommentComment
        fields = '__all__'
        read_only_fields = ('user', 'article_comment', )


# 댓글 < 대댓글
class ArticleCommentSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    comment_comments = ArticleCommentCommentSerializer(many=True, read_only=True)

    class Meta:
        model = ArticleComment
        fields = '__all__'
        read_only_fields = ('user', 'article', )


# 게시글 < 댓글 < 대댓글
class ArticleSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    comments = ArticleCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'good_users', 'bad_users', )

# 유저 프로필 페이지의 내가 쓴 댓글 및 대댓글 목록에 들어갈 serializers 미구현
# 대댓글 기능 모델 단위부터 재구성 고려
# 추후 fields 세분화 작업 요망