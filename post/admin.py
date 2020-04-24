from django.contrib import admin

from .models import *

from django.contrib.auth.mixins import LoginRequiredMixin


#class MyView(LoginRequiredMixin):
    #login_url = '/login/'
    #redirect_field_name = 'redirect_to'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title")
    list_display_links = ("author",)
    list_filter = ("topic",)
    search_fields = ("title", "text",)
    readonly_fields = ("author", "date_publish",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


