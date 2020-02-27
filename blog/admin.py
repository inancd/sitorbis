from django.contrib import admin
from blog.models import Post, PostCategory

admin.site.register(Post)
admin.site.register(PostCategory)