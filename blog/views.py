from django.shortcuts import render

from .models import Post


def post_list(request):
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts}
    return render(request, "blog/post_list.html", context)
