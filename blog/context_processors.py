from django.conf import settings
from django.shortcuts import get_object_or_404
from blog.models import Post

def blogs(request):
    publishing_blog = Post.objects.all()

    return {'blogs': publishing_blog}