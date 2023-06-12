from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Task

# Create your views here.


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def taskCompleted(request, pk):
    # Task.objects.filter(id=pk).update(is_completed=True)
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def tasknotCompleted(request, pk):
    # Task.objects.filter(id=pk).update(is_completed=True)
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def taskedit(request, pk):
    # Task.objects.filter(id=pk).update(is_completed=True)
    # task = get_object_or_404(Task, pk=pk)
    # task.task = request.POST['task']
    # task.save()
    # return redirect('home')
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        get_task.task = request.POST['task']
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)


def taskdelete(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()
    return redirect('home')
