from django.conf import settings
from django.shortcuts import get_object_or_404
from blog.models import Post, PostCategory

def blogs(request):
    publishing_blog = PostCategory.objects.all()

    return {'blogs': publishing_blog}