from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm

def task_list(request):
    q = request.GET.get('q', '')
    tasks = Task.objects.all().order_by('-created')
    if q:
        tasks = tasks.filter(title__icontains=q)
    form = TaskForm()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form, 'q': q})

@require_POST
def task_create(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('task_list')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})

@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
