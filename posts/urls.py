from django.urls import path

from .views import PostView,PostListView,CommentView,LikeView

urlpatterns = [
    path('post/', PostView.as_view(),name='post'),
    path('post/<int:post_pk>/', PostView.as_view(),name='post-detail'),
    path('post-list/', PostListView.as_view(),name='post-list'),
    path('post/<int:post_pk>/comments/',CommentView.as_view(),name='comments'),
    path('post/<int:post_pk>/Likes/',LikeView.as_view(),name='likes'),
]