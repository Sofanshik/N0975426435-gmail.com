from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    text = models.TextField(blank=True, db_index=True)
    date_publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)


#class User(models.Model):
    #first_name = models.CharField(max_length=30, db_index=True)
    #last_name = models.CharField(max_length=30, db_index=True)

    #def __str__(self):
       # return '{}'.format(self.first_name)

#class Topic(models.Model):
    #title = models.CharField(max_length=150, db_index=True)
    #slug = models.SlugField(max_length=150, unique=True)
    #value_of_post = models.IntegerField()

    #def __str__(self):
        #return '{}'.format(self.value_of_post)
