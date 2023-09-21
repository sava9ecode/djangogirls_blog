from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "text",
        )


class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
