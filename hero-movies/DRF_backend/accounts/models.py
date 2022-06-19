
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from movies.models import Movie


# Create your models here.
class User(AbstractUser):
    introduction = models.CharField(blank=True, null=True, max_length=200)
    profile_image = ResizedImageField(upload_to="profile_images", blank=True, null=True, size=[300, 300])

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # 회원가입시 받을 취향 영화
    # 영화 정보쪽에서 접근할 일이 없기 때문에 예외적으로 user 클래스에 작성
    fav_movies = models.ManyToManyField(Movie, related_name='fav_users')

    # <-- 역참조 리스트 -->

    # Movie.wished_movies
    # Vote.voted_movies

    # Article.articles
    # Article.article_goods
    # Article.article_bads
    # ArticleComment.article_comments
    # ArticleCommentComment.article_comment_comments

    # Review.reviews
    # Review.review_likes
    # ReviewComment.review_comments
    # ReviewComment.review_comment_likes
