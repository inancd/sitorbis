from django.contrib import admin
from blog.models import Post, PostCategory, Comment

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)