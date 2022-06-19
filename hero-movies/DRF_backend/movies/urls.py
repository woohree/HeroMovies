from . import views
from django.urls import path


app_name = 'movies'

urlpatterns = [
    # 영화 전체 목록
    path('', views.movie_list),
    # 추천 영화 목록
    path('recommended/', views.movie_recommendation),
    # 찜한 영화 목록 (위시리스트)
    path('wished/', views.wished_movie_list),
    # 평점 준 영화 목록
    path('voted/', views.voted_movie_list),

    # 영화 상세정보
    path('<int:movie_id>/', views.movie_detail),
    # 평점 생성, 수정, 삭제
    path('<int:movie_id>/voting/', views.create_or_update_or_delete_vote),
    # 찜하기 (위시리스트에 추가)
    path('<int:movie_id>/wishing/', views.add_or_cancel_wish),

    # 리뷰 
    path('<int:movie_id>/reviews/', views.movie_review_list_or_create),

    # 현재 로그인만 하면 가능, 어드민 유저만 가능하게 수정필
    path('test/import/', views.import_from_tmdb),
]
