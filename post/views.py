from django.shortcuts import render
from .forms import PostForm
from .models import *
from django.utils import timezone
from django.shortcuts import redirect
from django.db.models import Q, Count


def posts_list(request):
#   проверяем если пользователь выбрал топик то фильтруем посты по этому топику(query_params, url_param, параметры урл)

    topic = Topic.objects.all()

    search_guery = request.GET.get('search', '')

    if search_guery:
        posts = Post.objects.filter(Q(title__icontains=search_guery) | Q(text__icontains=search_guery))
    else:
        posts = Post.objects.all()

    return render(request, 'post/index.html', context={'posts': posts, 'topics': topic})


def post_detail(request, post_id):
    post_information = Post.objects.get(id=post_id)
    return render(request, 'post/post_detail.html', context={'post_information': post_information})


def topic_list(request):
    topics = Topic.objects.all().annotate(count_post=Count('posts'))

    return render(request, 'post/topic_list.html', context={'topics': topics})


def topic_detail(request, topic_id):
    topic_information = Topic.objects.get(id=topic_id)
    return render(request, 'post/topic_detail.html', context={'topic_information': topic_information})


def posts_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = post.date_publish
            post.save()
            return redirect('posts_detail_url', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'post/post_create.html', {'post_create': posts_create})
