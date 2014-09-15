from django.contrib import admin
from UWO_reddit_app.models import Category, SubCategory, Post, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Post)
admin.site.register(Comment)
