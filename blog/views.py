from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import RedirectView
from .models import Post, PostCategory

def Page(request):
    page_list = Post.objects.all()
    page_popular = Post.objects.filter(editor_featured=True)

    context = {
        'page': page_list,
        'slider': page_popular,
    }
    return render(request, 'blog/index.html', context)

def Category_view(request, slug):
    category = PostCategory.objects.filter(slug=slug)
    context = {
        'cat': category
    }
    return render(request, 'blog/category_detail.html', context)

def Detail_view(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)

    context = {
        'post': blog_post
    }
    return render(request, 'blog/blog_detail.html', context)





