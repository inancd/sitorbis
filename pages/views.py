from django.shortcuts import render, get_object_or_404
from .models import HomeClass
def pagehome(request):
    query = HomeClass.objects.all()

    context = {
        'query_list': query
    }
    return render(request, 'index.html', context)