from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', context={'posts': posts})


def post_detail(request, post_id):
    post_information = Post.objects.get(id=post_id)
    return render(request, 'post/post_detail.html', context={'post_information': post_information})


def posts_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = post.date_publish
            post.save()
            return redirect('post_detail', post_id=post.post_id)
    else:
        form = PostForm()
    return render(request, 'post/post_create.html', {'post_create': posts_create})
