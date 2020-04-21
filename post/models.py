from django.db import models
from django.conf import settings


class Topic(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return '{}'.format(self.name)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True)
    text = models.TextField(blank=True, db_index=True)
    date_publish = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField('Topic', blank=True, related_name='posts')

    def __str__(self):
        return '{}'.format(self.title)

