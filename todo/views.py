from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import TodoItem

# Create your views here.

def TodoView(request):

    all_todo_items = TodoItem.objects.all()
    context = {
        'query': all_todo_items
    }
    return render(request, 'todo/index.html', context)

def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, id):
    item_to_delete = TodoItem.objects.get(id=id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')