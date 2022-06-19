from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def article_list_or_create(request):
    articles = Article.objects.all()

    def article_list():
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def article_create():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == "GET":
        return article_list()
    elif request.method == "POST":
        return article_create()


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def article_update():
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def article_delete():
        article.delete()
        data = {
            "delete": f'article {article_id} is deleted'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    if request.method == "GET":
        return article_detail()
    elif request.method == "PUT":
        return article_update()
    elif request.method == "DELETE":
        return article_delete()


# only create, delete unavailable
@api_view(['POST'])
def article_good(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user not in article.good_users.all():
        article.good_users.add(request.user)
        article.save()
        data = {
            "good": f'{request.user} liked article(id={article.id})'
        }
    else:
        data = {
            "good": f'{request.user} already liked this article(id={article.id}) before'
        }
    return Response(data)
    
# only create, delete unavailable
@api_view(['POST'])
def article_bad(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user not in article.bad_users.all():
        article.bad_users.add(request.user)
        article.save()
        data = {
            "bad": f'{request.user} disliked article(id={article.id})'
        }
    else:
        data = {
            "bad": f'{request.user} already disliked article(id={article.id}) before'
        }
    return Response(data)


@api_view(['POST'])
def create_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    serializer = ArticleCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)

        comments = article.comments.all()
        serializer = ArticleCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, article_id, comment_id):
    article = get_object_or_404(Article, pk=article_id)
    article_comment = get_object_or_404(ArticleComment, pk=comment_id)
    comments = article.comments.all()

    def update_comment():
        serializer = ArticleCommentSerializer(instance=article_comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            serializer = ArticleCommentSerializer(comments, many=True)
            return Response(serializer.data)

    def delete_comment():
        article_comment.delete()
        # data = {
        #     "delete": f'comment {comment_id} is deleted'
        # }
        serializer = ArticleCommentSerializer(comments, many=True)
        return Response(serializer.data) # , status=status.HTTP_204_NO_CONTENT)

    if request.method == "PUT":
        return update_comment()
    elif request.method == "DELETE":
        return delete_comment()


@api_view(['POST'])
def create_comment_comment(request, article_id, comment_id):
    article = get_object_or_404(Article, pk=article_id)
    article_comment = get_object_or_404(ArticleComment, pk=comment_id)
    serializer = ArticleCommentCommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article_comment=article_comment)
        comments = article.comments.all()
        serializer = ArticleCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def update_or_delete_comment_comment(request, article_id, comment_comment_id):
    article = get_object_or_404(Article, pk=article_id)
    comment_comment = get_object_or_404(ArticleCommentComment, pk=comment_comment_id)

    def update_comment_comment():
        serializer = ArticleCommentCommentSerializer(instance=comment_comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_comment_comment():
        comment_comment.delete()
        # data = {
        #     "delete": f'comment_comment {comment_comment_id} is deleted'
        # }
        comments = article.comments.all()
        serializer = ArticleCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    if request.method == "PUT":
        return update_comment_comment()
    elif request.method == "DELETE":
        return delete_comment_comment()