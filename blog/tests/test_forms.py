from django.test import SimpleTestCase

from blog.forms import PostForm, CommentFrom


class PostFormTestCase(SimpleTestCase):
    def test_post_form_title_field_label(self):
        form = PostForm()
        self.assertEqual(form.fields["title"].label, "Title")

    def test_post_form_text_field_label(self):
        form = PostForm()
        self.assertEqual(form.fields["text"].label, "Text")


class CommentFormTestCase(SimpleTestCase):
    def test_comment_form_text_field_label(self):
        form = CommentFrom()
        self.assertEqual(form.fields["text"].label, "Text")
