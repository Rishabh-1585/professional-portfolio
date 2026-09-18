from django.shortcuts import render
from .models import BlogPost


def blog(request):
    posts = BlogPost.objects.filter(
        published=True
    ).order_by("-created_at")

    return render(
        request,
        "blog.html",
        {"posts": posts}
    )


def blog_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)

    return render(
        request,
        "blog_detail.html",
        {"post": post}
    )