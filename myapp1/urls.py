from django.urls import path
from myapp1 import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('video/create/', views.video_create, name='video_create'),
    path('video/<str:movie_id>/', views.video_detail, name='video_detail'),
    path('video/<str:movie_id>/edit/', views.video_update, name='video_update'),
    path('video/<str:movie_id>/delete/', views.video_delete, name='video_delete'),
]