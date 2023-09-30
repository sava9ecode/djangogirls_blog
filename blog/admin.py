from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = (
        "author",
        "created_date",
    )

    fieldsets = (
        (None, {"fields": ("author", "title", "text")}),
        ("Date", {"fields": ("created_date", "published_date")}),
    )

    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "author", "post")
    list_filter = (
        "author",
        "created_date",
    )

    fields = ["author", "post", "text", "created_date", "approved_comment"]
