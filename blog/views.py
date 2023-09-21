from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Post, Comment
from .forms import PostForm, CommentFrom


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()

    context = {"form": form}

    return render(request, "blog/post_edit.html", context)


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {"form": form}

    return render(request, "blog/post_edit.html", context)


@login_required
def post_draft_list(request):
    posts = (
        Post.objects.filter(published_date__isnull=True)
        .filter(author__exact=request.user)
        .order_by("-created_date")
    )
    context = {"posts": posts}
    return render(request, "blog/post_draft_list.html", context)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post_detail", pk=pk)


@login_required
def post_unpublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.unpublish()
    return redirect("post_detail", pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post_list")


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentFrom(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentFrom()

    context = {"form": form}

    return render(request, "blog/add_comment_to_post.html", context)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect("post_detail", pk=comment.post.pk)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect("post_detail", pk=comment.post.pk)


@login_required
def comment_unapprove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.unapprove()
    return redirect("post_detail", pk=comment.post.pk)


@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentFrom(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.save()
            return redirect("post_detail", pk=comment.post.pk)
    else:
        form = CommentFrom(instance=comment)

    context = {"form": form}

    return render(request, "blog/add_comment_to_post.html", context)
