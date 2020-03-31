from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import RedirectView
from django.db.models import Count
from .models import Post, PostCategory, Comment
from django.template.loader import render_to_string
from .forms import CommentForm

def Page(request):
    page_list = Post.objects.all()
    page_popular = Post.objects.filter(editor_featured=True).order_by("-dated_posted")
    popular_post = Post.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')[:5]

    context = {
        'page': page_list,
        'slider': page_popular,
        'popular_post': popular_post,
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
    comments = Comment.objects.filter(post=blog_post, reply=None).order_by('-id')
    is_liked = False

    if blog_post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=blog_post, user=request.user, content=content, reply=comment_qs)
            comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': blog_post,
        'is_liked': is_liked,
        'comments': comments,
        'comment_form': comment_form,

    }

    if request.is_ajax():
        html = render_to_string('blog/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'blog/blog_detail.html', context)


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    context = {
        'post': post,
        'is_liked': is_liked,
    }

    if request.is_ajax():
        html = render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form': html})