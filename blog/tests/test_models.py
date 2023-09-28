from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Post, Comment


class PostModelTestCase(TestCase):
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

    def test_author_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_text_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("text").verbose_name
        self.assertEqual(field_label, "text")

    def test_created_date_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("created_date").verbose_name
        self.assertEqual(field_label, "created date")

    def test_published_date_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field("published_date").verbose_name
        self.assertEqual(field_label, "published date")

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_str_representation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), "testtitle")

    def test_publish(self):
        post = Post.objects.get(id=1)
        post.publish()
        self.assertTrue(post.published_date)

    def test_unpublish(self):
        post = Post.objects.get(id=1)
        post.unpublish()
        self.assertFalse(post.published_date)

    def test_approved_comments(self):
        post = Post.objects.get(id=1)

        for i in range(5):
            Comment.objects.create(
                post=post,
                author="testauthor",
                text="testtext",
                approved_comment=False if i % 2 else True,
            )

        count_approved_comments = post.approved_comments().count()
        count_unapproved_comments = (
            post.comments.all().count() - count_approved_comments
        )
        self.assertEqual(count_approved_comments, 3)
        self.assertEqual(count_unapproved_comments, 2)


class CommentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            username="testusername",
            email="testemail@example.com",
            password="12345",
        )
        post = Post.objects.create(
            author=user,
            title="testtitle",
            text="testtext",
        )
        Comment.objects.create(
            post=post,
            author=user,
            text="testtext",
        )

    def test_post_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field("post").verbose_name
        self.assertEqual(field_label, "post")

    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field("text").verbose_name
        self.assertEqual(field_label, "text")

    def test_created_date_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field("created_date").verbose_name
        self.assertEqual(field_label, "created date")

    def test_approved_comment_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field("approved_comment").verbose_name
        self.assertEqual(field_label, "approved comment")

    def test_author_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field("author").max_length
        self.assertEqual(max_length, 200)

    def test_str_representation(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(str(comment), comment.text)

    def test_approve_comment(self):
        comment = Comment.objects.get(id=1)
        comment.approve()
        self.assertTrue(comment.approved_comment)

    def test_unapprove_comment(self):
        comment = Comment.objects.get(id=1)
        comment.approve()
        comment.unapprove()
        self.assertFalse(comment.approved_comment)
