from django.test import TestCase, RequestFactory
from .models import Post

from django.contrib.auth.models import User
from .views import PostListView, PostDetailView

class PostModelTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.user = User.objects.create_user(
            username="testuser",
            password="1234"
        )

        self.post = Post.objects.create(
            title="Test",
            content="Test content",
            author=self.user
        )

    def test_create_post(self):
        self.assertEqual(self.post.title, "Test")

    def test_PostListView(self):
        request = self.factory.get('/')
        response = PostListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_PostDetailView(self):
        # post = Post.objects.create(title="Test", content="Test content")
        request = self.factory.get(f'/post/{self.post.id}/')
        response = PostDetailView.as_view()(request, pk=self.post.id)
        self.assertEqual(response.status_code, 200)