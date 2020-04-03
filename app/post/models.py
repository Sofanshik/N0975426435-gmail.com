from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    text = models.TextField(blank=True, db_index=True)
    date_publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

class Topic(models.Model):
    name = models.CharField(max_length=50, db_index=True)