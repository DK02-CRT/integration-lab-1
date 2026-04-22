from django.urls import path
from .views import external_posts

urlpatterns = [
    path('external-posts/', external_posts, name='external_posts'),
]
