from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)


class SubCategory(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=400)


class Post(models.Model):
	subcatgegory = models.ForeignKey(SubCategory)
	title = models.CharField(max_length=200)
	time_posted = models.DateTimeField('Time Posted', auto_now_add=True)
	content = models.TextField()


class Comment(models.Model):
	post = models.ForeignKey(Post)
	time_commented = models.DateTimeField('Time Commented', auto_now_add=True)
	content = models.TextField()