from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoData

# Create your views here.
def index(request):
    tasks = ToDoData.objects.all()
    return render(request, 'todo/list.html', {
        'tasks': tasks
    })

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        ToDoData.objects.create(title=title)
        return redirect('todo:index')
    return render(request, 'todo/add.html')

def delete(request, id):
    ToDoData.objects.get(id=id).delete()
    return redirect('todo:index')
