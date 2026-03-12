from django.urls import path
from .views import PostListView, PostDetailView
from .views import posts_api

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('api/posts/', posts_api, name='posts_api'),
]