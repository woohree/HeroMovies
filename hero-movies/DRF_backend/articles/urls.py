from . import views
from django.urls import path


app_name = 'articles'

urlpatterns = [
    path('', views.article_list_or_create),
    path('<int:article_id>/', views.article_detail_or_update_or_delete),
    path('<int:article_id>/good/', views.article_good),
    path('<int:article_id>/bad/', views.article_bad),
    path('<int:article_id>/comments/', views.create_comment),
    path('<int:article_id>/comments/<int:comment_id>/', views.update_or_delete_comment),
    path('<int:article_id>/comments/<int:comment_id>/comment_comments/', views.create_comment_comment),
    path('<int:article_id>/comment_comments/<int:comment_comment_id>/', views.update_or_delete_comment_comment),
]
