from django.shortcuts import render, get_object_or_404
from .models import HomeClass, PrivacyClass, TermClass,StatementClass
from blog.models import Post
def pagehome(request):
    query = HomeClass.objects.all()
    page_popular = Post.objects.filter(editor_featured=True).order_by("-dated_posted")

    context = {
        'query_list': query,
        'slider': page_popular,
    }
    return render(request, 'index.html', context)

def term_views(request):
    query = get_object_or_404(TermClass)
    context = {
        'query': query
    }
    return render(request, 'terms.html', context)

def privacy_views(request):
    query = get_object_or_404(PrivacyClass)
    context = {
        'query': query
    }
    return render(request, 'privacy.html', context)

def statement_views(request):
    query = get_object_or_404(StatementClass)
    context = {
        'query': query
    }
    return render(request, 'statement.html', context)