from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('<post_id>', post_detail, name='posts_detail_url')
]