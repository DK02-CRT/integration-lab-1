from django.shortcuts import render
import requests


def external_posts(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    return render(request, "external_data/posts.html", {"posts": data[:7]})
