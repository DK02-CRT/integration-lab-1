from django.http import JsonResponse
# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


def posts_api(request):
    posts = Post.objects.all()

    data = []
    for post in posts:
        data.append({
            "id": post.id,
            "title": post.title,
            "content": post.content
        })

    return JsonResponse(data, safe=False)
