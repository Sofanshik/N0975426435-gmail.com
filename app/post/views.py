from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', context={'posts': posts})

def post_details(request, slug):
    post_information = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post_information': post_information})
