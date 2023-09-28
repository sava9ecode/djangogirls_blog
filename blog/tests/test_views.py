from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from blog.models import Post


class PostViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            username="testusername",
            email="testemail@example.com",
            password="12345",
        )
        
        Post.objects.create(
            author=user,
            title="testtitle",
            text="testtext",
        )

    def test_url_view_post_list_exists_at_desired_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_post_list_uses_correct_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_url_view_post_detail_exists_at_desired_location(self):
        post = get_object_or_404(Post, id=1)
        response = self.client.get(f"/post/{post.id}")
        self.assertEqual(response.status_code, 200)

    def test_view_post_detail_uses_correct_template(self):
        post = get_object_or_404(Post, id=1)
        response = self.client.get(f"/post/{post.id}")
        self.assertTemplateUsed(response, "blog/post_detail.html")
