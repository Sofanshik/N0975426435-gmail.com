from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('create/', posts_create, name='posts_create_url'),
    path('topics/', topic_list, name='list_of_topics_url'),
    path('topics/<topic_id>/', topic_detail, name='topics_detail_url'),
    path('<post_id>/', post_detail, name='posts_detail_url')
]