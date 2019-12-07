from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse



from .models import News, Category


# Create your views here.

def Page(request):
    queryset = News.objects.filter(featured=True)
    queryslider = News.objects.filter(slider_accept=True)

    context = {
        'news_list': queryset,
        'slider_list': queryslider
    }
    return render(request, 'news/index.html', context)

def Detail(request, news_slug):
    queryset = get_object_or_404(News, slug=news_slug)

    context = {
        'detail_list': queryset
    }
    return render(request, 'news/detail.html', context)

def CategoryDetail(request, slug):
    queryset = get_object_or_404(Category, slug=slug)

    context = {
        'category_list': queryset
    }
    return render(request, 'news/categorydetail.html', context)





