from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', context={'posts': posts})

def post_detail(request, post_id):
    post_information = Post.objects.get(id=post_id)
    return render(request, 'post/post_detail.html', context={'post_information': post_information})
