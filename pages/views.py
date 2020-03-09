from django.shortcuts import render, get_object_or_404
from .models import HomeClass
from blog.models import Post
def pagehome(request):
    query = HomeClass.objects.all()
    page_popular = Post.objects.filter(editor_featured=True).order_by("-dated_posted")

    context = {
        'query_list': query,
        'slider': page_popular,
    }
    return render(request, 'index.html', context)