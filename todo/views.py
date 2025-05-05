from django.shortcuts import render,redirect
from .models import Task

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title= request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'home.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('/')