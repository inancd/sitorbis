from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import RedirectView
from .models import Post, PostCategory

def Page(request):
    page_list = Post.objects.all()
    page_popular = Post.objects.filter(editor_featured=True).order_by("-dated_posted")
    popular_post = Post.objects.order_by('likes')[:5]

    context = {
        'page': page_list,
        'slider': page_popular,
        'popular_post': popular_post,
    }
    return render(request, 'blog/index.html', context)

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.slug)

def Category_view(request, slug):
    category = PostCategory.objects.filter(slug=slug)
    context = {
        'cat': category
    }
    return render(request, 'blog/category_detail.html', context)

def Detail_view(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)
    is_liked = False

    if blog_post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'post': blog_post,
        'is_liked': is_liked,

    }
    return render(request, 'blog/blog_detail.html', context)





