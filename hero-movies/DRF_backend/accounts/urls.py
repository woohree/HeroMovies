from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:user_id>/profile/', views.profile_detail_or_update),
    # path('favs/', views.fav_movies_create_or_update),
    path('favs/', views.fav_select_list),
    path('favs/create/', views.fav_create)
]
