from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
def Page(request):
    page_list = Post.objects.all()

    context = {
        'page': page_list
    }
    return render(request, 'blog/index.html', context)

def Detail_view(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)

    context = {
        'post': blog_post
    }
    return render(request, 'blog/blog_detail.html', context)

