from django.urls import path
from . import views
from .views import VideoList, VideoDetail, GenreListView
from commentcreate.views import CommentsCreate

urlpatterns = [
    path('', VideoList.as_view(), name='home'),
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('genre/<int:pk>/', GenreListView.as_view(), name='genre_list'),
    path('<int:pk>/', VideoDetail.as_view(), name='video'),
    path('<int:pk>/comment/create/', CommentsCreate.as_view(), name='comment_create'),
    # slug
    # path('<slug:slug>/', VideoDetail.as_view(), name='video'),
]
