from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    subcategory = models.ForeignKey(SubCategory)
    title = models.CharField(max_length=200)
    time_posted = models.DateTimeField('Time Posted', auto_now_add=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    time_commented = models.DateTimeField('Time Commented', auto_now_add=True)
    content = models.TextField()

    def __unicode__(self):
        return self.content
