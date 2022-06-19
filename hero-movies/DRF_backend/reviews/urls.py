from . import views
from django.urls import path


app_name = 'reviews'

urlpatterns = [
    # 게시판에서 리뷰 보거나 생성
    path('', views.review_list_or_create),
    path('<int:review_pk>/', views.review_detail_or_update_or_delete),
    path('<int:review_pk>/like/', views.review_like_or_cancel),
    path('<int:review_pk>/comments/', views.create_comment),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.update_or_delete_comment),
    path('comments/<int:comment_pk>/like/', views.comment_like_or_cancel),
]