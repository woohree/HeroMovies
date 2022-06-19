from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def review_list_or_create(request):
    reviews = Review.objects.all().order_by('-pk')

    def review_list():
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    # 사용자로부터 영화 pk를 같이 입력 받아야 함
    # {"reviewed_movie": <int:movie_id>} 이런식으로
    def review_create():
        serializer = ReviewCreateSerializer(data=request.data)
        movie = get_object_or_404(Movie, pk=request.data.get('reviewed_movie'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, reviewed_movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == "GET":
        return review_list()
    elif request.method == "POST":
        return review_create()


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def review_update():
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def review_delete():
        review.delete()
        data = {
            "delete": f'review {review_pk} is deleted'
        }
        return Response(data) #, status=status.HTTP_204_NO_CONTENT)

    if request.method == "GET":
        return review_detail()
    elif request.method == "PUT":
        return review_update()
    elif request.method == "DELETE":
        return review_delete()


@api_view(['PUT'])
def review_like_or_cancel(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    def review_like():
        review.like_users.add(request.user)
        review.save()
        data = {
            "like": f'{request.user} liked review {review.id}'
        }
        return Response(data)
    
    def review_like_cancel():
        review.like_users.remove(request.user)
        review.save()
        data = {
            "like": f'{request.user} canceled like on review {review.id}'
        }
        return Response(data)

    if request.user not in review.like_users.all():
        return review_like()
    else:
        return review_like_cancel()


@api_view(['POST'])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)

        comments = ReviewComment.objects.all()
        serializer = ReviewCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, review_pk, comment_pk):
    review_comment = get_object_or_404(ReviewComment, pk=comment_pk)
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comments.all()

    def update_comment():
        serializer = ReviewCommentSerializer(instance=review_comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            serializer = ReviewCommentSerializer(comments, many=True)
            return Response(serializer.data)

    def delete_comment():
        review_comment.delete()
        # data = {
        #     "delete": f'comment {comment_pk} is deleted'
        # }
        
        serializer = ReviewCommentSerializer(comments, many=True)
        return Response(serializer.data)#, status=status.HTTP_204_NO_CONTENT)

    if request.method == "PUT":
        return update_comment()
    elif request.method == "DELETE":
        return delete_comment()


@api_view(['PUT'])
def comment_like_or_cancel(request, comment_pk):
    comment = get_object_or_404(ReviewComment, pk=comment_pk)

    def comment_like():
        comment.like_users.add(request.user)
        comment.save()
        data = {
            "like": f'{request.user} liked comment {comment.id}'
        }
        return Response(data)
    
    def comment_like_cancel():
        comment.like_users.remove(request.user)
        comment.save()
        data = {
            "like": f'{request.user} canceled like on comment {comment.id}'
        }
        return Response(data)

    if request.user not in comment.like_users.all():
        return comment_like()
    else:
        return comment_like_cancel()
