from django.shortcuts import render, get_object_or_404

def pagehome(request):
    return render(request, 'index.html')